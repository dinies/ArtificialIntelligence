(define (problem vanilla-grid-1)
  (:domain vanilla-grid)
  (:objects node0-0 node0-1 node0-2 node0-3 node0-4 node0-5
            node1-0 node1-1 node1-2 node1-3 node1-4 node1-5
            node2-0 node2-1 node2-2 node2-3 node2-4 node2-5
            node3-0 node3-1 node3-2 node3-3 node3-4 node3-5
            node4-0 node4-1 node4-2 node4-3 node4-4 node4-5
            node5-0 node5-1 node5-2 node5-3 node5-4 node5-5
            robot )
  (:init
        
        (conn node0-0 node1-0)
        (conn node0-0 node0-1)
        (conn node0-1 node1-1)
        (conn node0-1 node0-2)
        (conn node0-1 node0-0)
        (conn node0-2 node1-2)
        (conn node0-2 node0-3)
        (conn node0-2 node0-1)
        (conn node0-3 node1-3)
        (conn node0-3 node0-4)
        (conn node0-3 node0-2)
        (conn node0-4 node1-4)
        (conn node0-4 node0-5)
        (conn node0-4 node0-3)
        (conn node0-5 node1-5)
        (conn node0-5 node0-4)
        (conn node1-0 node2-0)
        (conn node1-0 node0-0)
        (conn node1-0 node1-1)
        (conn node1-1 node2-1)
        (conn node1-1 node0-1)
        (conn node1-1 node1-2)
        (conn node1-1 node1-0)
        (conn node1-2 node2-2)
        (conn node1-2 node0-2)
        (conn node1-2 node1-3)
        (conn node1-2 node1-1)
        (conn node1-3 node2-3)
        (conn node1-3 node0-3)
        (conn node1-3 node1-4)
        (conn node1-3 node1-2)
        (conn node1-4 node2-4)
        (conn node1-4 node0-4)
        (conn node1-4 node1-5)
        (conn node1-4 node1-3)
        (conn node1-5 node2-5)
        (conn node1-5 node0-5)
        (conn node1-5 node1-4)
        (conn node2-0 node3-0)
        (conn node2-0 node1-0)
        (conn node2-0 node2-1)
        (conn node2-1 node3-1)
        (conn node2-1 node1-1)
        (conn node2-1 node2-2)
        (conn node2-1 node2-0)
        (conn node2-2 node3-2)
        (conn node2-2 node1-2)
        (conn node2-2 node2-3)
        (conn node2-2 node2-1)
        (conn node2-3 node3-3)
        (conn node2-3 node1-3)
        (conn node2-3 node2-4)
        (conn node2-3 node2-2)
        (conn node2-4 node3-4)
        (conn node2-4 node1-4)
        (conn node2-4 node2-5)
        (conn node2-4 node2-3)
        (conn node2-5 node3-5)
        (conn node2-5 node1-5)
        (conn node2-5 node2-4)
        (conn node3-0 node4-0)
        (conn node3-0 node2-0)
        (conn node3-0 node3-1)
        (conn node3-1 node4-1)
        (conn node3-1 node2-1)
        (conn node3-1 node3-2)
        (conn node3-1 node3-0)
        (conn node3-2 node4-2)
        (conn node3-2 node2-2)
        (conn node3-2 node3-3)
        (conn node3-2 node3-1)
        (conn node3-3 node4-3)
        (conn node3-3 node2-3)
        (conn node3-3 node3-4)
        (conn node3-3 node3-2)
        (conn node3-4 node4-4)
        (conn node3-4 node2-4)
        (conn node3-4 node3-5)
        (conn node3-4 node3-3)
        (conn node3-5 node4-5)
        (conn node3-5 node2-5)
        (conn node3-5 node3-4)
        (conn node4-0 node5-0)
        (conn node4-0 node3-0)
        (conn node4-0 node4-1)
        (conn node4-1 node5-1)
        (conn node4-1 node3-1)
        (conn node4-1 node4-2)
        (conn node4-1 node4-0)
        (conn node4-2 node5-2)
        (conn node4-2 node3-2)
        (conn node4-2 node4-3)
        (conn node4-2 node4-1)
        (conn node4-3 node5-3)
        (conn node4-3 node3-3)
        (conn node4-3 node4-4)
        (conn node4-3 node4-2)
        (conn node4-4 node5-4)
        (conn node4-4 node3-4)
        (conn node4-4 node4-5)
        (conn node4-4 node4-3)
        (conn node4-5 node5-5)
        (conn node4-5 node3-5)
        (conn node4-5 node4-4)
        (conn node5-0 node4-0)
        (conn node5-0 node5-1)
        (conn node5-1 node4-1)
        (conn node5-1 node5-2)
        (conn node5-1 node5-0)
        (conn node5-2 node4-2)
        (conn node5-2 node5-3)
        (conn node5-2 node5-1)
        (conn node5-3 node4-3)
        (conn node5-3 node5-4)
        (conn node5-3 node5-2)
        (conn node5-4 node4-4)
        (conn node5-4 node5-5)
        (conn node5-4 node5-3)
        (conn node5-5 node4-5)
        (conn node5-5 node5-4)

        (black node0-0)
        (black node0-1)
        (black node0-2)
        (black node0-3)
        (black node0-4)
        (black node0-5)
        (black node1-0)
        (white node1-1)
        (white node1-2)
        (black node1-3)
        (white node1-4)
        (black node1-5)
        (black node2-0)
        (white node2-1)
        (white node2-2)
        (white node2-3)
        (white node2-4)
        (black node2-5)
        (black node3-0)
        (black node3-1)
        (black node3-2)
        (black node3-3)
        (white node3-4)
        (black node3-5)
        (black node4-0)
        (white node4-1)
        (white node4-2)
        (white node4-3)
        (white node4-4)
        (black node4-5)
        (black node5-0)
        (black node5-1)
        (black node5-2)
        (black node5-3)
        (black node5-4)
        (black node5-5)
        (at robot node1-1 )
  )
  (:goal (at robot node4-1)
  )
)
