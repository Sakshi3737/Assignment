# Assignment

Q.1] Signals executes synchronously by default
Visit : https://127.0.0.1:8000/sync/
Console: Before save
        Signal stated (wait  5 sec)
        Signal finished
        After save
Proof : After save prints only after signal execution completes that menas signal are synchronous


Q.2] Signals run in the same thread
Visit : http://127.0.0.1:8000/thread/
Console: Main thread ID : 14532
        Signal Thread ID : 14532
Proof: Both IDs are identical. Signals run in the same thread

Q.3] Signals run in the same transaction
Visit: http://127.0.0.1:8000/transaction/
Output : 
    Records save: 0
Proof : Teh transaction rolled back and record disapperaed that menas signal runs wuithin the same database transaction by default.
