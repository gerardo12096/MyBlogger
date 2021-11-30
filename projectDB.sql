INSERT INTO `users` (username,password,first_name,last_name,email) VALUES ('batman','1234','bat','bat','nananana@batman.com'),
('bob','12345','bob','bob','bobthatsme@yahoo.com'),
('catlover','abcd','cat','cat','catlover@whiskers.com'),
('doglover','efds','dog','dog','doglover@bark.net'),
('jdoe','25478','joe','jod','jane@doe.com'),
('jsmith','1111','john','smith','jsmith@gmail.com'),
('matty','2222','mat','mat','matty@csun.edu'),
('notbob','5555','not','bob','stopcallingmebob@yahoo.com'),
('pacman','9999','pacman','pacman','pacman@gmail.com'),
('scooby','8888','scoby','scoby','scooby@doo.net');

INSERT INTO `post` (id, subject, description, date_created, created_by, author) VALUES 
(2,'Hello World','Hey everyone, this is my first blog. Hello world and all who inhabit it!','2020-03-15','jsmith','7'),
(3,'I love cats!','Cats are amazing. Theyre awesome, and fuzzy, and cute. Who DOESNT love cats?','2020-03-17','catlover','4'),
(4,'Dogs are the best.','So I saw a post the other day talking about cats. Now, I love cats. Theyre great. But heres the thing: dogs are just the best, okay? Theres no question about it. That is all.','2020-03-19','doglover','5'),
(5,'I am the night.','To all you lowly criminals out there, this isa warning to know I am watching. I am justice. I am righteousness. I am the NIGHT.','2020-03-24','batman','2'),
(6,'Waka waka','waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka','2020-03-31','pacman','10'),
(7,'Who is this Bob guy?','Decided to start tracking down this mysterious human known as Bob. Who is Bob? What does he do? WHY does he do it? There is a lot of mystery surrounding this person, and I will be going into detail in future posts. Stay tuned!','2020-04-02','notbob','3'),
(8,'Re: I love cats.','A reader recently reached out to me about my last post. To be clear, Im not dissing our canine companions! But weve got to be honest here, why are cats better? Theyre smart, affectionate, and great cuddle partners. Cats are better. Its just fact.','2020-04-04','catlover','4'),
(9,'Scooby Dooby Doo!','The search for scooby snacks: Where did they go? I know this whole quarantine thing is affecting businesses, but arent scooby snacks counted as an essential service? Please post below if you find anything! Im going crazy here!','2020-04-05','scooby','11'),
(10,'Bob Update','Dear readers, I know you have been waiting anxiously for an update on Bob, but there is 
not much to share so far. He appears to have little to no online presence. Just a clarification: I am decidedly NOT Bob. Thanks all. Stay tuned for more!','2020-04-06','notbob','9'),
(11,'Lizard People.','What are your guys thoughts on them? I, for one, welcome out reptitlian overlords.','2020-04-12','jdoe','6');

INSERT INTO `tag`(text, author, post_id) VALUES ('helloworld','7','2'),
('animals','3','3'),('cats','3','3'),
('animals','4','4'),('dogs','4','4'),('crime','5','5'),('justice','5','5'),('cartoon','6','6'),('waka','6','6'),
('bob','7','7'),('update','7','7'),('cats','8','8'),('dogs','8','8'),('dogs','9','9'),('quarantine','9','9'),('scooby
snacks','9','9'),('bob','10','10'),('update','10','10'),('lizards','10','11');


INSERT INTO `comment`(sentiment, text, date_created, post_id, author) VALUES 
('negative','Cats are cool and all, but dogs are where its at.','2020-03-17','3','5'),
('negative','Whats all the hype about? Cats are clearly superior.','2020-03-20',3,'4'),
('positive','Nice.','2020-03-20',4,'11'),
('positive','Who IS Bob? I cant wait to find out.','2020-04-02','7','7'),
('negative','I guess cat people just dont know what theyre missing.','2020-04-05','3','5'),
('positive','This is totally unrelated, but I just wanted to say I am a HUGE fan of yours. I love your work!','2020-04-05','9','5'),
('positive','Have you checked out Dog-Mart? Theyve got everything.','2020-04-06','9','8'),
('negative','I was hopingnthered be more of an update. Sorry, Bob.','2020-04-07','10','7'),
('positive','I think theyre all secretly cats. Open your eyes, sheeple!','2020-04-13','11','5'),
('negative','Who? Me? Multimillionaire philanthropist of Arkham? A lizard person? Nope. Nothing to see here!','2020-04-15','5','2');



-- INSERT INTO `blogs` VALUES (1,'Hello World','Hey everyone, this is my first blog. 
-- Hello world and all who inhabit it!','2020-03-15','jsmith'),(2,'I love cats!','Cats
-- are amazing. They\'re awesome, and fuzzy, and cute. Who DOESN\'T love cats?','2020-
-- 03-17','catlover'),(3,'Dogs are the best.','So I saw a post the other day talking 
-- about cats. Now, I love cats. They\'re great. But here\'s the thing: dogs are just 
-- the best, okay? There\'s no question about it. That is all.','2020-03-
-- 19','doglover'),(4,'I am the night.','To all you lowly criminals out there, this is
-- a warning to know I am watching. I am justice. I am righteousness. I am the 
-- NIGHT.','2020-03-24','batman'),(5,'Waka waka','waka waka waka waka waka waka waka 
-- waka waka waka waka waka waka waka waka waka','2020-03-31','pacman'),(6,'Who is 
-- this Bob guy?','Decided to start tracking down this mysterious human known 
-- as \'Bob.\' Who is Bob? What does he do? WHY does he do it? There is a lot of 
-- mystery surrounding this person, and I will be going into detail in future posts. 
-- Stay tuned!','2020-04-02','notbob'),(7,'Re: I love cats.','A reader recently 
-- reached out to me about my last post. To be clear, I\'m not dissing our canine 
-- companions! But we\'ve got to be honest here, why are cats better? They\'re smart, 
-- affectionate, and great cuddle partners. Cats are better. It\'s just fact.','2020-
-- 04-04','catlover'),(8,'Scooby Dooby Doo!','The search for scooby snacks: Where did 
-- they go? I know this whole quarantine thing is affecting businesses, but aren\'t 
-- scooby snacks counted as an essential service? Please post below if you find 
-- anything! I\'m going crazy here!','2020-04-05','scooby'),(9,'Bob Update','Dear 
-- readers, I know you have been waiting anxiously for an update on Bob, but there is 
-- not much to share so far. He appears to have little to no online presence. Just a 
-- clarification: I am decidedly NOT Bob. Thanks all. Stay tuned for more!','2020-04-
-- 06','notbob'),(10,'Lizard People.','What are your guys thoughts on them? I, for 
-- one, welcome out reptitlian overlords.','2020-04-12','jdoe');

-- -- CREATE TABLE `blogstags` (
-- --   `blogid` int(10) unsigned NOT NULL,
-- --   `tag` varchar(20) NOT NULL,
-- --   PRIMARY KEY (`blogid`,`tag`),
-- --   CONSTRAINT `blogstags_ibfk_1` FOREIGN KEY (`blogid`) REFERENCES `blogs` 
-- -- (`blogid`)
-- -- )
-- -- INSERT INTO `blogstags` VALUES (1,'hello world'),(2,'animals'),(2,'cats'),
-- -- (3,'animals'),(3,'dogs'),(4,'crime'),(4,'justice'),(5,'cartoon'),(5,'waka'),
-- -- (6,'bob'),(6,'update'),(7,'cats'),(7,'dogs'),(8,'dogs'),(8,'quarantine'),(8,'scooby
-- -- snacks'),(9,'bob'),(9,'update'),(10,'lizards');
-- -- INSERT INTO `comments` VALUES (1,'negative','Cats are cool and all, but dogs are 
-- -- where it\'s at.','2020-03-17',2,'doglover'),(2,'negative','What\'s all the hype 
-- -- about? Cats are clearly superior.','2020-03-20',3,'catlover'),
-- -- (3,'positive','Nice.','2020-03-20',4,'scooby'),(4,'positive','Who IS Bob? I can\'t 
-- -- wait to find out.','2020-04-02',6,'jsmith'),(5,'negative','I guess cat people just 
-- -- don\'t know what they\'re missing.','2020-04-05',7,'doglover'),(6,'positive','This 
-- -- is totally unrelated, but I just wanted to say I am a HUGE fan of yours. I love 
-- -- your work!','2020-04-05',8,'doglover'),(7,'positive','Have you checked out Dog-
-- -- Mart? They\'ve got everything.','2020-04-06',8,'matty'),(8,'negative','I was hoping
-- -- there\'d be more of an update. Sorry, Bob.','2020-04-07',9,'jsmith'),
-- -- (9,'positive','I think they\re all secretly cats. Open your eyes, sheeple!','2020-
-- -- 04-13',10,'doglover'),(10,'negative','Who? Me? Multimillionaire philanthropist of 
-- -- Arkham? A lizard person? Nope. Nothing to see here!','2020-04-15',10,'batman');
-- -- CREATE TABLE `follows` (
-- --   `leadername` varchar(45) NOT NULL,
-- --   `followername` varchar(45) NOT NULL,
-- --   PRIMARY KEY (`leadername`,`followername`),
-- --   KEY `follows_ibfk_2` (`followername`),
-- --   CONSTRAINT `follows_ibfk_1` FOREIGN KEY (`leadername`) REFERENCES `users` 
-- -- (`username`),
-- --   CONSTRAINT `follows_ibfk_2` FOREIGN KEY (`followername`) REFERENCES `users` 
-- -- (`username`)
-- -- );
-- -- INSERT INTO `follows` VALUES ('jsmith','bob'),('batman','catlover'),
-- -- ('doglover','catlover'),('pacman','catlover'),('catlover','doglover'),
-- -- ('jsmith','jdoe'),('bob','notbob'),('jdoe','notbob'),('batman','pacman'),
-- -- ('scooby','pacman'),('doglover','scooby'),('pacman','scooby');
-- -- DROP TABLE IF EXISTS `hobbies`;
-- -- CREATE TABLE `hobbies` (
-- --   `username` varchar(45) NOT NULL,
-- --   `hobby` varchar(20) NOT NULL,
-- --   PRIMARY KEY (`hobby`,`username`),
-- --   KEY `hobbies_ibfk_1` (`username`),
-- --   CONSTRAINT `hobbies_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` 
-- -- (`username`),
-- --   CONSTRAINT `hobby_types` CHECK ((`hobby` in 
-- -- (_utf8mb4'hiking',_utf8mb4'swimming',_utf8mb4'calligraphy',_utf8mb4'bowling',_utf8m
-- -- b4'movie',_utf8mb4'cooking',_utf8mb4'dancing')))
-- -- );
-- -- INSERT INTO `hobbies` VALUES ('batman','movie'),('bob','movie'),
-- -- ('catlover','movie'),('doglover','hiking'),('jdoe','dancing'),('jdoe','movie'),
-- -- ('jsmith','hiking'),('matty','bowling'),('notbob','calligraphy'),
-- -- ('pacman','dancing'),('pacman','movie'),('scooby','cooking');