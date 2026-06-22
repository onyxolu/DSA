class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list of pre-requisites
        prereq = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        #  A Course has three possible states
        # visited => Course has been added to output
        # visiting => Course not added to output but added to cycle
        # unvisited => Course not added to output or cycle

        output = []
        visit, cycle = set(), set()

        # Can I safely complete this course, and what must I finish before it?
        def dfs(crs):
            # Found a cycle: impossible to finish all courses
            if crs in cycle:
                return False

            # Already processed this course
            if crs in visit:
                return True

            # Mark as currently being explored
            cycle.add(crs)

            # Process all prerequisites first
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            # Finished exploring this course
            cycle.remove(crs)
            visit.add(crs)

            # Add course after its prerequisites
            output.append(crs)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output