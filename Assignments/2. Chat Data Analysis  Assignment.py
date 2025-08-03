n = int(input("Enter the number of messages: "))
chat_dict = {}
messages = []
users = set()
total_words = 0
max_word_count = 0
longest_message = ""
message_counts = {}

for _ in range(n):
    chat = input().strip()
    if ':' not in chat:
        continue
    name, message = chat.split(":", 1)
    name = name.strip()
    message = message.strip()

    if name not in chat_dict:
        chat_dict[name] = []
    chat_dict[name].append(message)

    users.add(name)
    messages.append((name, message))

    if name not in message_counts:
        message_counts[name] = 0
    message_counts[name] += 1

    total_words += len(message.split())

print(f"Total number of messages:{len(messages)}")
sorted_users = list(users)
sorted_users.sort()
print("Unique users in the chat:", set(sorted_users))
print(f"Total words of chat:{total_words}")

if len(messages) > 0:
    avg = total_words / len(messages)
else:
    avg = 0
print(f"Average words per message: {avg:.2f}")

for i in range(len(messages)):
    sender = messages[i][0]
    message = messages[i][1]
    current_word_count = len(message.split())
    if current_word_count > max_word_count:
        max_word_count = current_word_count
        longest_message = sender + ": " + message

print(f"The longest message is: {longest_message}")
most_active_user = ""
max_messages = 0
for user in message_counts:
    if message_counts[user] > max_messages:
        max_messages = message_counts[user]
        most_active_user = user

print(f"most active user : {most_active_user} ({max_messages} messages)")

user_check = input().strip()
if user_check in message_counts:
    specific_user_message_count = message_counts[user_check]
    mention_count = message_counts[user_check]
    print(f"Messages sent by {user_check} : {specific_user_message_count}")
    print(f"Messages mentioning '{user_check}' : {mention_count}")
else:
    print(f"{user_check} not found in the chat history.")

target_user = input().strip()
if target_user not in chat_dict:
    print(f"{target_user} not found.")
else:
    all_messages = ""
    for msg in chat_dict[target_user]:
        all_messages += msg + " "
    word_list = all_messages.strip().split()

    word_freq = {}
    for word in word_list:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    most_common_word = ""
    most_common_count = 0
    for word in word_freq:
        if word_freq[word] > most_common_count:
            most_common_count = word_freq[word]
            most_common_word = word

    repeated_words = []
    for word in word_freq:
        if word_freq[word] > 1:
            repeated_words.append(word)

    print(f"Most Frequently used word by {target_user} : \"{most_common_word}\"")
    print(f"Common repeated words: {set(repeated_words)}")

target_user = input().strip()
if target_user in chat_dict:
    print(f"First message by {target_user}: \"{chat_dict[target_user][0]}\"")
    print(f"Last message by {target_user}: \"{chat_dict[target_user][-1]}\"")
else:
    print(f"User {target_user} not found in the chat.")

check_user = input().strip()
if check_user in chat_dict:
    print(f"User {check_user} found in the chat.")
else:
    print(f"User {check_user} not found in the chat.")
user_avg_len = {}
for user in chat_dict:
    messages_list = chat_dict[user]
    word_total = 0
    for msg in messages_list:
        word_total += len(msg.split())
    avg_len = word_total / len(messages_list)
    user_avg_len[user] = avg_len

longest_user = ""
longest_avg = 0
for user in user_avg_len:
    if user_avg_len[user] > longest_avg:
        longest_avg = user_avg_len[user]
        longest_user = user
print(f"User with longest average message: {longest_user} (avg {round(longest_avg,1)} words)")
unique_messages = []
for msg in messages:
    if msg not in unique_messages:
        unique_messages.append(msg)
print(f"Unique messages count: {len(unique_messages)}")
for i in range(len(messages)):
    for j in range(i + 1, len(messages)):
        if messages[i][1].lower() > messages[j][1].lower():
            temp = messages[i]
            messages[i] = messages[j]
            messages[j] = temp

print("Messages sorted alphabetically: ")
for msg in messages:
    print(f"{msg[0]}: {msg[1]}")
user1 = input().strip()
user2 = input().strip()
reply_count = 0
for i in range(1, len(messages)):
    prev_user = messages[i - 1][0]
    current_user = messages[i][0]
    if prev_user == user1 and current_user == user2:
        reply_count += 1
print(f"Reply ratio from {user2} to {user1}: {reply_count} replies")
deleted_keywords = {"message deleted", "<deleted>", ""}
deleted_count = 0
for _, msg in messages:
    if msg.strip().lower() in deleted_keywords:
        deleted_count += 1
print(f"Total deleted messages: {deleted_count}")
questions_found = False
for name, msg in messages:
    if '?' in msg:
        print(f"{name}: {msg}")
        questions_found = True
if not questions_found:
    print("No questions found in the chat.")
