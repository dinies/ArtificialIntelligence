
(define (problem babby)
  (:domain babby-grid)
  (:objects node0-0 node0-1 node0-2 node0-3 node0-4 node0-5 node0-6 node0-7 node0-8 node0-9 node0-10 node0-11
            node1-0 node1-1 node1-2 node1-3 node1-4 node1-5 node1-6 node1-7 node1-8 node1-9 node1-10 node1-11
            node2-0 node2-1 node2-2 node2-3 node2-4 node2-5 node2-6 node2-7 node2-8 node2-9 node2-10 node2-11
            node3-0 node3-1 node3-2 node3-3 node3-4 node3-5 node3-6 node3-7 node3-8 node3-9 node3-10 node3-11
            node4-0 node4-1 node4-2 node4-3 node4-4 node4-5 node4-6 node4-7 node4-8 node4-9 node4-10 node4-11
            node5-0 node5-1 node5-2 node5-3 node5-4 node5-5 node5-6 node5-7 node5-8 node5-9 node5-10 node5-11
            node6-0 node6-1 node6-2 node6-3 node6-4 node6-5 node6-6 node6-7 node6-8 node6-9 node6-10 node6-11
            node7-0 node7-1 node7-2 node7-3 node7-4 node7-5 node7-6 node7-7 node7-8 node7-9 node7-10 node7-11
            node8-0 node8-1 node8-2 node8-3 node8-4 node8-5 node8-6 node8-7 node8-8 node8-9 node8-10 node8-11
            node9-0 node9-1 node9-2 node9-3 node9-4 node9-5 node9-6 node9-7 node9-8 node9-9 node9-10 node9-11
            node10-0 node10-1 node10-2 node10-3 node10-4 node10-5 node10-6 node10-7 node10-8 node10-9 node10-10 node10-11
            node11-0 node11-1 node11-2 node11-3 node11-4 node11-5 node11-6 node11-7 node11-8 node11-9 node11-10 node11-11
            robot1 tray1 tray2 cloth1 )
  (:init
        (conn node0-0 node1-0) (conn node0-0 node0-1)
        (conn node0-1 node0-0) (conn node0-1 node1-1) (conn node0-1 node0-2)
        (conn node0-2 node0-1) (conn node0-2 node1-2) (conn node0-2 node0-3)
        (conn node0-3 node0-2) (conn node0-3 node1-3) (conn node0-3 node0-4)
        (conn node0-4 node0-3) (conn node0-4 node1-4) (conn node0-4 node0-5)
        (conn node0-5 node0-4) (conn node0-5 node1-5) (conn node0-5 node0-6)
        (conn node0-6 node0-5) (conn node0-6 node1-6) (conn node0-6 node0-7)
        (conn node0-7 node0-6) (conn node0-7 node1-7) (conn node0-7 node0-8)
        (conn node0-8 node0-7) (conn node0-8 node1-8) (conn node0-8 node0-9)
        (conn node0-9 node0-8) (conn node0-9 node1-9) (conn node0-9 node0-10)
        (conn node0-10 node0-9) (conn node0-10 node1-10) (conn node0-10 node0-11)
        (conn node0-11 node0-10) (conn node0-11 node1-11)

        (conn node1-0 node2-0) (conn node1-0 node1-1) (conn node1-0 node0-0)
        (conn node1-1 node1-0) (conn node1-1 node2-1) (conn node1-1 node1-2) (conn node1-1 node0-1)
        (conn node1-2 node1-1) (conn node1-2 node2-2) (conn node1-2 node1-3) (conn node1-2 node0-2)
        (conn node1-3 node1-2) (conn node1-3 node2-3) (conn node1-3 node1-4) (conn node1-3 node0-3)
        (conn node1-4 node1-3) (conn node1-4 node2-4) (conn node1-4 node1-5) (conn node1-4 node0-4)
        (conn node1-5 node1-4) (conn node1-5 node2-5) (conn node1-5 node1-6) (conn node1-5 node0-5)
        (conn node1-6 node1-5) (conn node1-6 node2-6) (conn node1-6 node1-7) (conn node1-6 node0-6)
        (conn node1-7 node1-6) (conn node1-7 node2-7) (conn node1-7 node1-8) (conn node1-7 node0-7)
        (conn node1-8 node1-7) (conn node1-8 node2-8) (conn node1-8 node1-9) (conn node1-8 node0-8)
        (conn node1-9 node1-8) (conn node1-9 node2-9) (conn node1-9 node1-10) (conn node1-9 node0-9)
        (conn node1-10 node1-9) (conn node1-10 node2-10) (conn node1-10 node1-11) (conn node1-10 node0-10)
        (conn node1-11 node1-10) (conn node1-11 node2-11) (conn node1-11 node0-11)


        (conn node2-0 node3-0) (conn node2-0 node2-1) (conn node2-0 node1-0)
        (conn node2-1 node2-0) (conn node2-1 node3-1) (conn node2-1 node2-2) (conn node2-1 node1-1)
        (conn node2-2 node2-1) (conn node2-2 node3-2) (conn node2-2 node2-3) (conn node2-2 node1-2)
        (conn node2-3 node2-2) (conn node2-3 node3-3) (conn node2-3 node2-4) (conn node2-3 node1-3)
        (conn node2-4 node2-3) (conn node2-4 node3-4) (conn node2-4 node2-5) (conn node2-4 node1-4)
        (conn node2-5 node2-4) (conn node2-5 node3-5) (conn node2-5 node2-6) (conn node2-5 node1-5)
        (conn node2-6 node2-5) (conn node2-6 node3-6) (conn node2-6 node2-7) (conn node2-6 node1-6)
        (conn node2-7 node2-6) (conn node2-7 node3-7) (conn node2-7 node2-8) (conn node2-7 node1-7)
        (conn node2-8 node2-7) (conn node2-8 node3-8) (conn node2-8 node2-9) (conn node2-8 node1-8)
        (conn node2-9 node2-8) (conn node2-9 node3-9) (conn node2-9 node2-10) (conn node2-9 node1-9)
        (conn node2-10 node2-9) (conn node2-10 node3-10) (conn node2-10 node2-11) (conn node2-10 node1-10)
        (conn node2-11 node2-10) (conn node2-11 node3-11) (conn node2-11 node1-11)


        (conn node3-0 node4-0) (conn node3-0 node3-1) (conn node3-0 node2-0)
        (conn node3-1 node3-0) (conn node3-1 node4-1) (conn node3-1 node3-2) (conn node3-1 node2-1)
        (conn node3-2 node3-1) (conn node3-2 node4-2) (conn node3-2 node3-3) (conn node3-2 node2-2)
        (conn node3-3 node3-2) (conn node3-3 node4-3) (conn node3-3 node3-4) (conn node3-3 node2-3)
        (conn node3-4 node3-3) (conn node3-4 node4-4) (conn node3-4 node3-5) (conn node3-4 node2-4)
        (conn node3-5 node3-4) (conn node3-5 node4-5) (conn node3-5 node3-6) (conn node3-5 node2-5)
        (conn node3-6 node3-5) (conn node3-6 node4-6) (conn node3-6 node3-7) (conn node3-6 node2-6)
        (conn node3-7 node3-6) (conn node3-7 node4-7) (conn node3-7 node3-8) (conn node3-7 node2-7)
        (conn node3-8 node3-7) (conn node3-8 node4-8) (conn node3-8 node3-9) (conn node3-8 node2-8)
        (conn node3-9 node3-8) (conn node3-9 node4-9) (conn node3-9 node3-10) (conn node3-9 node2-9)
        (conn node3-10 node3-9) (conn node3-10 node4-10) (conn node3-10 node3-11) (conn node3-10 node2-10)
        (conn node3-11 node3-10) (conn node3-11 node4-11) (conn node3-11 node2-11)


        (conn node4-0 node5-0) (conn node4-0 node4-1) (conn node4-0 node3-0)
        (conn node4-1 node4-0) (conn node4-1 node5-1) (conn node4-1 node4-2) (conn node4-1 node3-1)
        (conn node4-2 node4-1) (conn node4-2 node5-2) (conn node4-2 node4-3) (conn node4-2 node3-2)
        (conn node4-3 node4-2) (conn node4-3 node5-3) (conn node4-3 node4-4) (conn node4-3 node3-3)
        (conn node4-4 node4-3) (conn node4-4 node5-4) (conn node4-4 node4-5) (conn node4-4 node3-4)
        (conn node4-5 node4-4) (conn node4-5 node5-5) (conn node4-5 node4-6) (conn node4-5 node3-5)
        (conn node4-6 node4-5) (conn node4-6 node5-6) (conn node4-6 node4-7) (conn node4-6 node3-6)
        (conn node4-7 node4-6) (conn node4-7 node5-7) (conn node4-7 node4-8) (conn node4-7 node3-7)
        (conn node4-8 node4-7) (conn node4-8 node5-8) (conn node4-8 node4-9) (conn node4-8 node3-8)
        (conn node4-9 node4-8) (conn node4-9 node5-9) (conn node4-9 node4-10) (conn node4-9 node3-9)
        (conn node4-10 node4-9) (conn node4-10 node5-10) (conn node4-10 node4-11) (conn node4-10 node3-10)
        (conn node4-11 node4-10) (conn node4-11 node5-11) (conn node4-11 node3-11)

        (conn node5-0 node6-0) (conn node5-0 node5-1) (conn node5-0 node4-0)
        (conn node5-1 node5-0) (conn node5-1 node6-1) (conn node5-1 node5-2) (conn node5-1 node4-1)
        (conn node5-2 node5-1) (conn node5-2 node6-2) (conn node5-2 node5-3) (conn node5-2 node4-2)
        (conn node5-3 node5-2) (conn node5-3 node6-3) (conn node5-3 node5-4) (conn node5-3 node4-3)
        (conn node5-4 node5-3) (conn node5-4 node6-4) (conn node5-4 node5-5) (conn node5-4 node4-4)
        (conn node5-5 node5-4) (conn node5-5 node6-5) (conn node5-5 node5-6) (conn node5-5 node4-5)
        (conn node5-6 node5-5) (conn node5-6 node6-6) (conn node5-6 node5-7) (conn node5-6 node4-6)
        (conn node5-7 node5-6) (conn node5-7 node6-7) (conn node5-7 node5-8) (conn node5-7 node4-7)
        (conn node5-8 node5-7) (conn node5-8 node6-8) (conn node5-8 node5-9) (conn node5-8 node4-8)
        (conn node5-9 node5-8) (conn node5-9 node6-9) (conn node5-9 node5-10) (conn node5-9 node4-9)
        (conn node5-10 node5-9) (conn node5-10 node6-10) (conn node5-10 node5-11) (conn node5-10 node4-10)
        (conn node5-11 node5-10) (conn node5-11 node6-11) (conn node5-11 node4-11)

        (conn node6-0 node7-0) (conn node6-0 node6-1) (conn node6-0 node5-0)
        (conn node6-1 node6-0) (conn node6-1 node7-1) (conn node6-1 node6-2) (conn node6-1 node5-1)
        (conn node6-2 node6-1) (conn node6-2 node7-2) (conn node6-2 node6-3) (conn node6-2 node5-2)
        (conn node6-3 node6-2) (conn node6-3 node7-3) (conn node6-3 node6-4) (conn node6-3 node5-3)
        (conn node6-4 node6-3) (conn node6-4 node7-4) (conn node6-4 node6-5) (conn node6-4 node5-4)
        (conn node6-5 node6-4) (conn node6-5 node7-5) (conn node6-5 node6-6) (conn node6-5 node5-5)
        (conn node6-6 node6-5) (conn node6-6 node7-6) (conn node6-6 node6-7) (conn node6-6 node5-6)
        (conn node6-7 node6-6) (conn node6-7 node7-7) (conn node6-7 node6-8) (conn node6-7 node5-7)
        (conn node6-8 node6-7) (conn node6-8 node7-8) (conn node6-8 node6-9) (conn node6-8 node5-8)
        (conn node6-9 node6-8) (conn node6-9 node7-9) (conn node6-9 node6-10) (conn node6-9 node5-9)
        (conn node6-10 node6-9) (conn node6-10 node7-10) (conn node6-10 node6-11) (conn node6-10 node5-10)
        (conn node6-11 node6-10) (conn node6-11 node7-11) (conn node6-11 node5-11)


        (conn node7-0 node8-0) (conn node7-0 node7-1) (conn node7-0 node6-0)
        (conn node7-1 node7-0) (conn node7-1 node8-1) (conn node7-1 node7-2) (conn node7-1 node6-1)
        (conn node7-2 node7-1) (conn node7-2 node8-2) (conn node7-2 node7-3) (conn node7-2 node6-2)
        (conn node7-3 node7-2) (conn node7-3 node8-3) (conn node7-3 node7-4) (conn node7-3 node6-3)
        (conn node7-4 node7-3) (conn node7-4 node8-4) (conn node7-4 node7-5) (conn node7-4 node6-4)
        (conn node7-5 node7-4) (conn node7-5 node8-5) (conn node7-5 node7-6) (conn node7-5 node6-5)
        (conn node7-6 node7-5) (conn node7-6 node8-6) (conn node7-6 node7-7) (conn node7-6 node6-6)
        (conn node7-7 node7-6) (conn node7-7 node8-7) (conn node7-7 node7-8) (conn node7-7 node6-7)
        (conn node7-8 node7-7) (conn node7-8 node8-8) (conn node7-8 node7-9) (conn node7-8 node6-8)
        (conn node7-9 node7-8) (conn node7-9 node8-9) (conn node7-9 node7-10) (conn node7-9 node6-9)
        (conn node7-10 node7-9) (conn node7-10 node8-10) (conn node7-10 node7-11) (conn node7-10 node6-10)
        (conn node7-11 node7-10) (conn node7-11 node8-11) (conn node7-11 node6-11)



        (conn node8-0 node9-0) (conn node8-0 node8-1) (conn node8-0 node7-0)
        (conn node8-1 node8-0) (conn node8-1 node9-1) (conn node8-1 node8-2) (conn node8-1 node7-1)
        (conn node8-2 node8-1) (conn node8-2 node9-2) (conn node8-2 node8-3) (conn node8-2 node7-2)
        (conn node8-3 node8-2) (conn node8-3 node9-3) (conn node8-3 node8-4) (conn node8-3 node7-3)
        (conn node8-4 node8-3) (conn node8-4 node9-4) (conn node8-4 node8-5) (conn node8-4 node7-4)
        (conn node8-5 node8-4) (conn node8-5 node9-5) (conn node8-5 node8-6) (conn node8-5 node7-5)
        (conn node8-6 node8-5) (conn node8-6 node9-6) (conn node8-6 node8-7) (conn node8-6 node7-6)
        (conn node8-7 node8-6) (conn node8-7 node9-7) (conn node8-7 node8-8) (conn node8-7 node7-7)
        (conn node8-8 node8-7) (conn node8-8 node9-8) (conn node8-8 node8-9) (conn node8-8 node7-8)
        (conn node8-9 node8-8) (conn node8-9 node9-9) (conn node8-9 node8-10) (conn node8-9 node7-9)
        (conn node8-10 node8-9) (conn node8-10 node9-10) (conn node8-10 node8-11) (conn node8-10 node7-10)
        (conn node8-11 node8-10) (conn node8-11 node9-11) (conn node8-11 node7-11)



        (conn node9-0 node10-0) (conn node9-0 node9-1) (conn node9-0 node8-0)
        (conn node9-1 node9-0) (conn node9-1 node10-1) (conn node9-1 node9-2) (conn node9-1 node8-1)
        (conn node9-2 node9-1) (conn node9-2 node10-2) (conn node9-2 node9-3) (conn node9-2 node8-2)
        (conn node9-3 node9-2) (conn node9-3 node10-3) (conn node9-3 node9-4) (conn node9-3 node8-3)
        (conn node9-4 node9-3) (conn node9-4 node10-4) (conn node9-4 node9-5) (conn node9-4 node8-4)
        (conn node9-5 node9-4) (conn node9-5 node10-5) (conn node9-5 node9-6) (conn node9-5 node8-5)
        (conn node9-6 node9-5) (conn node9-6 node10-6) (conn node9-6 node9-7) (conn node9-6 node8-6)
        (conn node9-7 node9-6) (conn node9-7 node10-7) (conn node9-7 node9-8) (conn node9-7 node8-7)
        (conn node9-8 node9-7) (conn node9-8 node10-8) (conn node9-8 node9-9) (conn node9-8 node8-8)
        (conn node9-9 node9-8) (conn node9-9 node10-9) (conn node9-9 node9-10) (conn node9-9 node8-9)
        (conn node9-10 node9-9) (conn node9-10 node10-10) (conn node9-10 node9-11) (conn node9-10 node8-10)
        (conn node9-11 node9-10) (conn node9-11 node10-11) (conn node9-11 node8-11)



        (conn node10-0 node11-0) (conn node10-0 node10-1) (conn node10-0 node9-0)
        (conn node10-1 node10-0) (conn node10-1 node11-1) (conn node10-1 node10-2) (conn node10-1 node9-1)
        (conn node10-2 node10-1) (conn node10-2 node11-2) (conn node10-2 node10-3) (conn node10-2 node9-2)
        (conn node10-3 node10-2) (conn node10-3 node11-3) (conn node10-3 node10-4) (conn node10-3 node9-3)
        (conn node10-4 node10-3) (conn node10-4 node11-4) (conn node10-4 node10-5) (conn node10-4 node9-4)
        (conn node10-5 node10-4) (conn node10-5 node11-5) (conn node10-5 node10-6) (conn node10-5 node9-5)
        (conn node10-6 node10-5) (conn node10-6 node11-6) (conn node10-6 node10-7) (conn node10-6 node9-6)
        (conn node10-7 node10-6) (conn node10-7 node11-7) (conn node10-7 node10-8) (conn node10-7 node9-7)
        (conn node10-8 node10-7) (conn node10-8 node11-8) (conn node10-8 node10-9) (conn node10-8 node9-8)
        (conn node10-9 node10-8) (conn node10-9 node11-9) (conn node10-9 node10-10) (conn node10-9 node9-9)
        (conn node10-10 node10-9) (conn node10-10 node11-10) (conn node10-10 node10-11) (conn node10-10 node9-10)
        (conn node10-11 node10-10) (conn node10-11 node11-11) (conn node10-11 node9-11)



        (conn node11-0 node11-1) (conn node11-0 node10-0)
        (conn node11-1 node11-0) (conn node11-1 node11-1) (conn node11-1 node10-2)
        (conn node11-2 node11-1) (conn node11-2 node11-2) (conn node11-2 node10-3)
        (conn node11-3 node11-2) (conn node11-3 node11-3) (conn node11-3 node10-4)
        (conn node11-4 node11-3) (conn node11-4 node11-4) (conn node11-4 node10-5)
        (conn node11-5 node11-4) (conn node11-5 node11-5) (conn node11-5 node10-6)
        (conn node11-6 node11-5) (conn node11-6 node11-6) (conn node11-6 node10-7)
        (conn node11-7 node11-6) (conn node11-7 node11-7) (conn node11-7 node10-8)
        (conn node11-8 node11-7) (conn node11-8 node11-8) (conn node11-8 node10-9)
        (conn node11-9 node11-8) (conn node11-9 node11-9) (conn node11-9 node10-10)
        (conn node11-10 node11-9) (conn node11-10 node11-10) (conn node11-10 node10-11)
        (conn node11-11 node11-10) (conn node11-11 node10-11)

        (black node0-0)
        (black node0-1)
        (black node0-2)
        (black node0-3)
        (black node0-4)
        (black node0-5)
        (black node0-6)
        (black node0-7)
        (black node0-8)
        (black node0-9)
        (black node0-10)
        (black node0-11)

        (black node11-0)
        (black node11-1)
        (black node11-2)
        (black node11-3)
        (black node11-4)
        (black node11-5)
        (black node11-6)
        (black node11-7)
        (black node11-8)
        (black node11-9)
        (black node11-10)
        (black node11-11)

        (black node1-11)
        (black node2-11)
        (black node3-11)
        (black node4-11)
        (black node5-11)
        (black node6-11)
        (black node7-11)
        (black node8-11)
        (black node9-11)
        (black node10-11)

        (black node1-0)
        (black node2-0)
        (black node3-0)
        (black node4-0)
        (black node5-0)
        (black node6-0)
        (black node7-0)
        (black node8-0)
        (black node9-0)
        (black node10-0)




        (seat node3-3)
        (seat node2-4)
        (table node2-3)
        (dishwasher node9-8)
        (washingmachine node2-9)
        (closet node6-9)




        (white node1-10) (white node2-10) (black node3-10) (white node4-10) (black node5-10) (white node6-10) (white node7-10) (white node8-10) (white node9-10) (white node10-10)
        (white node1-9)                   (black node3-9)  (white node4-9)  (black node5-9)                   (white node7-9)  (white node8-9)  (white node9-9)  (white node10-9)
        (white node1-8)  (white node2-8)  (black node3-8)  (white node4-8)  (white node5-8)  (white node6-8)  (white node7-8)  (white node8-8)                   (white node10-8)
        (white node1-7)  (white node2-7)  (white node3-7)  (white node4-7)  (black node5-7)  (white node6-7)  (white node7-7)  (white node8-7)  (white node9-7)  (white node10-7)
        (black node1-6)  (black node2-6)  (black node3-6)  (white node4-6)  (black node5-6)  (black node6-6)  (black node7-6)  (black node8-6)  (black node9-6)  (black node10-6)
        (white node1-5)  (white node2-5)  (white node3-5)  (white node4-5)  (white node5-5)  (white node6-5)  (white node7-5)  (white node8-5)  (white node9-5)  (white node10-5)
        (white node1-4)                   (white node3-4)  (white node4-4)  (white node5-4)  (white node6-4)  (white node7-4)  (white node8-4)  (white node9-4)  (white node10-4)
        (white node1-3)                                    (white node4-3)  (white node5-3)  (white node6-3)  (white node7-3)  (white node8-3)  (white node9-3)  (white node10-3)
        (white node1-2)  (white node2-2)  (white node3-2)  (white node4-2)  (white node5-2)  (white node6-2)  (white node7-2)  (white node8-2)  (white node9-2)  (white node10-2)
        (white node1-1)  (white node2-1)  (white node3-1)  (white node4-1)  (white node5-1)  (white node6-1)  (white node7-1)  (white node8-1)  (white node9-1)  (white node10-1)






        (at robot1 node7-1 )
        (tray tray1)
        (at tray1 node3-3)
        (tray tray2)
        (at tray2 node2-4)
        (cloth cloth1)
        (at cloth1 node2-3)
        (robot robot1)
  )
(:goal (and (at tray1 node6-9)
            (at tray2 node6-9)
            (at cloth1 node2-3)
            (clean tray1)
            (clean tray2)
            (clean cloth1)
))
)
