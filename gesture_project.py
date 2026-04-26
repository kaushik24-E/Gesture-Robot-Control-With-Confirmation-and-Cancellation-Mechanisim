PLUGIN_META = {
    "name": "Gesture Control with Confirm & Cancel",
    "description": "Finger counting with confirmation and cancel system",
}

LAST_TRIGGER_KEY = None
LAST_TRIGGER_AT = 0
STABILITY = {}
COOLDOWN_MS = 1200
REQUIRED_STABLE_FRAMES = 2


def setup(payload):
    global LAST_TRIGGER_KEY, LAST_TRIGGER_AT, STABILITY
    LAST_TRIGGER_KEY = None
    LAST_TRIGGER_AT = 0
    STABILITY = {}
    return {"status": "Plugin ready"}


def operation_by_index(frame, index):
    saved = frame.get("saved_operations", [])
    if index is None or index < 0 or index >= len(saved):
        return None
    return saved[index]


def count_fingers(hand):
    return hand.get("fingerCountNoThumb", 0)


def update_stability(key):
    global STABILITY
    STABILITY[key] = STABILITY.get(key, 0) + 1
    return STABILITY[key]


def is_open_palm(hand):
    return hand.get("fingerCountNoThumb", 0) >= 4


def process_frame(frame):
    global LAST_TRIGGER_KEY, LAST_TRIGGER_AT, STABILITY

    hands = frame.get("hands", [])

    if not hands:
        STABILITY = {}
        return {
            "label": "No hand detected",
            "confidence": 0.0
        }

    left_hand = None
    right_hand = None

    for hand in hands:
        if hand.get("handedness") == "Left":
            left_hand = hand
        elif hand.get("handedness") == "Right":
            right_hand = hand

    if not left_hand:
        return {
            "label": "Show LEFT hand for command",
            "confidence": 0.5
        }

    count = count_fingers(left_hand)

    if count == 1:
        action = "Forward"
        index = 0
    elif count == 2:
        action = "Left"
        index = 1
    elif count == 3:
        action = "Right"
        index = 2
    elif count >= 4:
        action = "Stop"
        index = 3
    else:
        action = "None"
        index = None

    operation = operation_by_index(frame, index)

    confirm = False
    cancel = False

    if right_hand:
        if right_hand.get("fingerCountNoThumb", 0) == 0:
            confirm = True
        elif is_open_palm(right_hand):
            cancel = True

    key = f"{action}:{confirm}:{cancel}"
    stable_frames = update_stability(key)

    now = frame.get("timestamp_ms", 0)

    should_trigger = (
        operation is not None
        and confirm
        and not cancel
        and stable_frames >= REQUIRED_STABLE_FRAMES
        and (key != LAST_TRIGGER_KEY or now - LAST_TRIGGER_AT > COOLDOWN_MS)
    )

    if should_trigger:
        LAST_TRIGGER_KEY = key
        LAST_TRIGGER_AT = now

    return {
        "label": f"Action: {action} | Confirm: {confirm} | Cancel: {cancel}",
        "confidence": 0.9 if count > 0 else 0.5,
        "trigger_operation_id": operation["id"] if should_trigger and operation else None,
        "debug_text": [
            f"Left hand count: {count}",
            f"Confirm (fist): {confirm}",
            f"Cancel (open palm): {cancel}",
            f"Stable frames: {stable_frames}"
        ]
    }