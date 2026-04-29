from random import random

class TicketCounterSimulation:

    def _handleArrival(self, curTime):
        # Penumpang datang secara acak
        if random() <= self._arriveProb:
            passenger = Passenger(curTime)
            self._passengerQ.enqueue(passenger)
            self._numPassengers += 1

    def _handleBeginService(self, curTime):
        # Agen mulai melayani jika tersedia
        for agent in self._theAgents:
            if agent.isFree() and not self._passengerQ.isEmpty():
                passenger = self._passengerQ.dequeue()
                agent.startService(passenger, curTime + self._serviceTime)
                self._totalWaitTime += curTime - passenger.timeArrived()

    def _handleEndService(self, curTime):
        # Mengecek agen yang selesai
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                agent.stopService()