from collections import defaultdict, Counter
n=int(input("Enter the number of messages: "))
chat_dict=defaultdict(list)
messages=[]
users=set()
total_words=0
max_word_count=0
longest_message=""
message_counts=defaultdict(int)
for _ in range(n):
    chat=input().strip()
    if ':' not in chat:
        continue
    name,message=chat.split(":",1)
    name=name.strip()
    message=message.strip()
    chat_dict[name].append(message)
    users.add(name)
    messages.append((name,message))
    message_counts[name]+=1
    total_words+=len(message.split())
print(f"Total number of messages:{len(messages)}")
print("Unique users in the chat:",set(sorted(users)))
print(f"Total words of chat:{total_words}")
avg=total_words/len(messages)
print(F"Average words per message: {avg:.2f}")
for sender,message in messages:
    current_word_count=len(message.split())
    if current_word_count>max_word_count:
        max_word_count=current_word_count
        longest_message=f"{sender}: {message}"
print(f"The longest message is: {longest_message}")
most_active_user=max(message_counts,key=message_counts.get)
print(f"most active user : {most_active_user} ({message_counts[most_active_user]} messages)")
user_check=input().strip()
if user_check in message_counts:
    specific_user_message_count=message_counts[user_check]
    mention_count=message_counts[user_check]
    print(f"Messages sent by {user_check} : {specific_user_message_count}")
    print(f"Messages mentioning '{user_check}' : {mention_count}")
else:
    print(f"{user_check} not found in the chat history.")
target_user=input().strip()
if target_user not in chat_dict:
    print(f"{target_user} not found.")
else:
    all_messages=" ".join(chat_dict[target_user])
    word_counts=Counter(all_messages.split())
    most_common_word=word_counts.most_common(1)[0][0]
    repeated_words = {word for word, count in word_counts.items() if count > 1}
    print(f"Most Frequently used word by {target_user} : \"{most_common_word}\"")
    print(f"Common repeated words: {repeated_words}")
target_user=input().strip()
if target_user in chat_dict:
    print(f"First message by {target_user}: \"{chat_dict[target_user][0]}\"")
    print(f"Last message by {target_user}: \"{chat_dict[target_user][-1]}\"")
else:
    print(f"User {target_user} not found in the chat.")
check_user=input().strip()
if check_user in chat_dict:
    print(f"User {check_user} found in the chat.")
else:
    print(f"User {check_user} not found in the chat.")
user_avg_len={}
for user in chat_dict:
    messages_list=chat_dict[user]
    word_total=sum(len(msg.split()) for msg in messages_list)
    user_avg_len[user]=word_total/len(messages_list)
longest_user=max(user_avg_len,key=user_avg_len.get)
longest_avg=round(user_avg_len[longest_user],1)
print(f"User with longest average message: {longest_user} (avg {longest_avg} words)")
unique_messages=set(messages)
print(f"Unique messages count: {len(unique_messages)}")
sorted_messages=sorted(messages,key=lambda x:x[1].lower())
print("Messages sorted alphabetically: ")
for msg in sorted_messages:
    print(f"{msg[:]}")
user1=input().strip()
user2=input().strip()
reply_count=0
total_replied_messages=0
for i in range(1, len(messages)):
    prev_user=messages[i-1][0]
    current_user=messages[i][0]
    if prev_user==user1 and current_user==user2:
        reply_count += 1
print(f"Reply ratio from {user2} to {user1}: {reply_count} replies")
deleted_keywords = {"message deleted", "<deleted>", ""}
deleted_count=sum(1 for _, msg in messages if msg.strip().lower() in deleted_keywords)
print(f"Total deleted messages: {deleted_count}")
questions = [f"{name}: {msg}" for name, msg in messages if '?' in msg]
if questions:
    for q in questions:
        print(q)
else:
    print("No questions found in the chat.")
