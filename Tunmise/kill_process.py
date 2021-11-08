import collections
import deque
class ProcessKiller():
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_dictionary = collections.defaultdict(list)
        output = []
        next_process_to_kill = deque([kill])

        for p in range(len(ppid)):
            parent_dictionary[ppid[p]].append(pid[p])

        while(next_process_to_kill):
            kill_proc = next_process_to_kill.pop()
            output.append(kill_proc)
            for process in parent_dictionary[kill_proc]:
                next_process_to_kill.append(process)

        return output