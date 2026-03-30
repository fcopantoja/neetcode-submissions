class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Contar frecuencia de cada tarea
        counter = Counter(tasks)
        
        # Crear un max heap usando valores negativos (porque heapq es min heap)
        max_heap = [cnt * -1 for cnt in counter.values()]
        
        # Cola para manejar tareas en cooldown -> [remaining_count, available_time]
        q = deque()
        
        # Convertir lista en heap
        heapq.heapify(max_heap)
        
        time = 0  # contador de tiempo (intervalos)

        # Mientras haya tareas pendientes en heap o en cooldown
        while max_heap or q:
            time += 1  # avanzamos el tiempo en cada iteración
            
            if max_heap:
                # Tomamos la tarea con mayor frecuencia
                cnt = 1 + heapq.heappop(max_heap)  # sumamos 1 porque es negativo
                
                # Si aún quedan ejecuciones de esta tarea
                if cnt:
                    # La metemos en cooldown con el tiempo en que estará disponible otra vez
                    q.append([cnt, time + n])
            
            # Si la tarea en cooldown ya puede volver al heap
            if q and q[0][1] == time:
                item = q.popleft()
                heapq.heappush(max_heap, item[0])
        
        return time