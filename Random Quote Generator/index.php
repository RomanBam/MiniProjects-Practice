<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Quote Generator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Random Quote Generator</h1>
        
        <?php
        $quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "Life is what happens to you while you're busy making other plans. - John Lennon",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "It is during our darkest moments that we must focus to see the light. - Aristotle",
            "The way to get started is to quit talking and begin doing. - Walt Disney",
            "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
            "If you really look closely, most overnight successes took a long time. - Steve Jobs",
            "The only impossible journey is the one you never begin. - Tony Robbins",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
            "Go confidently in the direction of your dreams! Live the life you've imagined. - Henry David Thoreau",
            "When you have a dream, you've got to grab it and never let go. - Carol Burnett",
            "Nothing is impossible, the word itself says 'I'm possible'! - Audrey Hepburn",
            "There is nothing impossible to they who will try. - Alexander the Great"
        ];
        
        $randomIndex = array_rand($quotes);
        $selectedQuote = $quotes[$randomIndex];
        
        $quoteParts = explode(' - ', $selectedQuote);
        $quoteText = $quoteParts[0];
        $quoteAuthor = $quoteParts[1];
        ?>
        
        <div class="quote-container">
            <blockquote class="quote">
                "<?php echo $quoteText; ?>"
            </blockquote>
            <cite class="author">— <?php echo $quoteAuthor; ?></cite>
        </div>
        
        <div class="actions">
            <a href="index.php" class="new-quote-btn">Get New Quote</a>
            <button onclick="copyQuote()" class="copy-btn">Copy Quote</button>
        </div>
        
        <div class="stats">
            <p>Total Quotes Available: <strong><?php echo count($quotes); ?></strong></p>
            <p>Current Quote #<?php echo $randomIndex + 1; ?></p>
        </div>
    </div>
    
    <script>
        function copyQuote() {
            const quoteText = document.querySelector('.quote').textContent;
            const author = document.querySelector('.author').textContent;
            const fullQuote = quoteText + ' ' + author;
            
            navigator.clipboard.writeText(fullQuote).then(function() {
                alert('Quote copied to clipboard!');
            });
        }
    </script>
</body>
</html>
