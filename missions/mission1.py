import time
from transitions import Machine


class Mission1:
    def __init__(self):
        mission_1_states = [
            'ms_s',  # ms_s - Marker Search State
            'mm_s',  # mm_s - Moving to Marker State
        ]
        mission_1_transitions = [
            {
                'trigger': 'fm_t',  # fm_t - Found Marker Trigger, means, AUV will go forward for 1 seconds
                'source': 'ms_s',
                'dest': 'mm_s',
            },
            {
                'trigger': 'ms_t',  # ms_t - Marker Search Trigger, means, AUV will spin around itself 0.25 seconds
                'source': 'mm_s',
                'dest': 'ms_s',
            }
        ]
        self.machine = Machine(
            model=self,
            states=mission_1_states,
            transitions=mission_1_transitions,
            name="Mission 1",
            initial='ms_s'
        )

    def on_enter_ms_s(self):
        print('MISSION 1 TRIGGER: "Marker Search Trigger"')
        time.sleep(1)
        self.fm_t()

    def on_enter_mm_s(self):
        print('MISSION 1 TRIGGER: "Moving to Marker State"')
        time.sleep(1)
        self.ms_t()
