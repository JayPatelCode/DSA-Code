from collections import deque
dq=deque([])
dq.append(12)
dq.append(18)
dq.appendleft(11)
# dq.pop()
dq.popleft()
print(dq)




# =============================================
# UNDERSTANDING THE DIFFERENCE
# =============================================

print("🔍 WHAT MAKES DEQUE SPECIAL:")
print("• popleft() - Remove from LEFT end in O(1)")
print("• pop() - Remove from RIGHT end in O(1)") 
print("• appendleft() - Add to LEFT end in O(1)")
print("• append() - Add to RIGHT end in O(1)")
print("")

print("❌ WHAT'S SLOW WITH REGULAR LISTS:")
print("• list.pop(0) - Remove from LEFT end in O(n) - SLOW!")
print("• list.insert(0, item) - Add to LEFT end in O(n) - SLOW!")
print("• list.pop() - Remove from RIGHT end in O(1) - Fast")
print("• list.append(item) - Add to RIGHT end in O(1) - Fast")
print("")

# =============================================
# VISUAL REPRESENTATION
# =============================================

print("=== VISUAL: HOW DEQUE WORKS ===")
print("")
print("DEQUE (Double-Ended Queue):")
print("┌─────────────────────────────────────────┐")
print("│  LEFT END    [1][2][3][4][5]   RIGHT END │")
print("│     ↑                            ↑      │") 
print("│  popleft()                    pop()     │")
print("│ appendleft()                 append()   │")
print("│   O(1)                        O(1)     │")
print("└─────────────────────────────────────────┘")
print("")