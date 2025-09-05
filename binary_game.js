import readline from "readline"

// ANSI color codes for terminal styling
const colors = {
  reset: "\x1b[0m",
  bright: "\x1b[1m",
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  blue: "\x1b[34m",
  magenta: "\x1b[35m",
  cyan: "\x1b[36m",
  white: "\x1b[37m",
}

class BinaryGame {
  constructor() {
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    })

    this.score = 0
    this.totalQuestions = 0
    this.difficulty = "easy"
    this.gameMode = "mixed"
  }

  // Generate random number based on difficulty
  generateNumber() {
    const ranges = {
      easy: { min: 1, max: 15 }, // 4-bit numbers
      medium: { min: 16, max: 255 }, // 8-bit numbers
      hard: { min: 256, max: 1023 }, // 10-bit numbers
    }

    const range = ranges[this.difficulty]
    return Math.floor(Math.random() * (range.max - range.min + 1)) + range.min
  }

  // Convert decimal to binary
  decToBin(decimal) {
    return decimal.toString(2)
  }

  // Convert binary to decimal
  binToDec(binary) {
    return Number.parseInt(binary, 2)
  }

  // Display game header
  showHeader() {
    console.clear()
    console.log(`${colors.cyan}${colors.bright}
    ╔══════════════════════════════════════╗
    ║           🔢 BINARY GAME 🔢          ║
    ║                                      ║
    ║     Master the Art of Binary!        ║
    ╚══════════════════════════════════════╝${colors.reset}
    `)
    console.log(
      `${colors.yellow}Score: ${this.score}/${this.totalQuestions} | Difficulty: ${this.difficulty.toUpperCase()} | Mode: ${this.gameMode.toUpperCase()}${colors.reset}\n`,
    )
  }

  // Show main menu
  async showMenu() {
    this.showHeader()
    console.log(`${colors.white}Choose an option:${colors.reset}`)
    console.log(`${colors.green}1.${colors.reset} Start Game`)
    console.log(`${colors.blue}2.${colors.reset} Change Difficulty (Current: ${this.difficulty})`)
    console.log(`${colors.magenta}3.${colors.reset} Change Mode (Current: ${this.gameMode})`)
    console.log(`${colors.yellow}4.${colors.reset} How to Play`)
    console.log(`${colors.red}5.${colors.reset} Quit\n`)

    const choice = await this.askQuestion("Enter your choice (1-5): ")

    switch (choice.trim()) {
      case "1":
        await this.startGame()
        break
      case "2":
        await this.changeDifficulty()
        break
      case "3":
        await this.changeMode()
        break
      case "4":
        await this.showInstructions()
        break
      case "5":
        this.quit()
        break
      default:
        console.log(`${colors.red}Invalid choice! Please try again.${colors.reset}`)
        await this.delay(1000)
        await this.showMenu()
    }
  }

  // Change difficulty level
  async changeDifficulty() {
    this.showHeader()
    console.log(`${colors.white}Select Difficulty:${colors.reset}`)
    console.log(`${colors.green}1.${colors.reset} Easy (1-15) - 4-bit numbers`)
    console.log(`${colors.yellow}2.${colors.reset} Medium (16-255) - 8-bit numbers`)
    console.log(`${colors.red}3.${colors.reset} Hard (256-1023) - 10-bit numbers\n`)

    const choice = await this.askQuestion("Enter your choice (1-3): ")

    switch (choice.trim()) {
      case "1":
        this.difficulty = "easy"
        break
      case "2":
        this.difficulty = "medium"
        break
      case "3":
        this.difficulty = "hard"
        break
      default:
        console.log(`${colors.red}Invalid choice!${colors.reset}`)
        await this.delay(1000)
        await this.changeDifficulty()
        return
    }

    console.log(`${colors.green}Difficulty set to ${this.difficulty.toUpperCase()}!${colors.reset}`)
    await this.delay(1000)
    await this.showMenu()
  }

  // Change game mode
  async changeMode() {
    this.showHeader()
    console.log(`${colors.white}Select Game Mode:${colors.reset}`)
    console.log(`${colors.green}1.${colors.reset} Mixed - Both decimal to binary and binary to decimal`)
    console.log(`${colors.blue}2.${colors.reset} Decimal to Binary - Convert decimal numbers to binary`)
    console.log(`${colors.magenta}3.${colors.reset} Binary to Decimal - Convert binary numbers to decimal\n`)

    const choice = await this.askQuestion("Enter your choice (1-3): ")

    switch (choice.trim()) {
      case "1":
        this.gameMode = "mixed"
        break
      case "2":
        this.gameMode = "dec2bin"
        break
      case "3":
        this.gameMode = "bin2dec"
        break
      default:
        console.log(`${colors.red}Invalid choice!${colors.reset}`)
        await this.delay(1000)
        await this.changeMode()
        return
    }

    console.log(`${colors.green}Game mode set to ${this.gameMode.toUpperCase()}!${colors.reset}`)
    await this.delay(1000)
    await this.showMenu()
  }

  // Show game instructions
  async showInstructions() {
    this.showHeader()
    console.log(`${colors.white}${colors.bright}HOW TO PLAY:${colors.reset}\n`)
    console.log(`${colors.cyan}🎯 Goal:${colors.reset} Convert between binary and decimal numbers correctly!`)
    console.log(`${colors.cyan}📊 Scoring:${colors.reset} Get points for each correct answer`)
    console.log(`${colors.cyan}⚡ Modes:${colors.reset}`)
    console.log(`   • Mixed: Both conversion types`)
    console.log(`   • Decimal to Binary: Convert numbers like 10 → 1010`)
    console.log(`   • Binary to Decimal: Convert numbers like 1010 → 10`)
    console.log(`${colors.cyan}🎚️ Difficulty:${colors.reset}`)
    console.log(`   • Easy: 1-15 (4-bit)`)
    console.log(`   • Medium: 16-255 (8-bit)`)
    console.log(`   • Hard: 256-1023 (10-bit)`)
    console.log(`\n${colors.yellow}💡 Tip: Remember that each binary digit represents a power of 2!${colors.reset}`)
    console.log(`${colors.yellow}   Example: 1010 = 1×8 + 0×4 + 1×2 + 0×1 = 10${colors.reset}\n`)

    await this.askQuestion("Press Enter to continue...")
    await this.showMenu()
  }

  // Start the main game loop
  async startGame() {
    console.log(`${colors.green}${colors.bright}🎮 Starting Binary Game! 🎮${colors.reset}\n`)
    console.log(`${colors.yellow}Type 'quit' at any time to return to menu${colors.reset}\n`)

    while (true) {
      const continueGame = await this.playRound()
      if (!continueGame) break

      console.log(`\n${colors.cyan}Current Score: ${this.score}/${this.totalQuestions}${colors.reset}`)
      const playAgain = await this.askQuestion("\nContinue playing? (y/n): ")
      if (playAgain.toLowerCase() !== "y" && playAgain.toLowerCase() !== "yes") {
        break
      }
      console.log("")
    }

    await this.showFinalScore()
    await this.showMenu()
  }

  // Play a single round
  async playRound() {
    const number = this.generateNumber()
    let questionType

    // Determine question type based on game mode
    if (this.gameMode === "mixed") {
      questionType = Math.random() < 0.5 ? "dec2bin" : "bin2dec"
    } else {
      questionType = this.gameMode
    }

    let question, correctAnswer, userAnswer

    if (questionType === "dec2bin") {
      question = `Convert ${colors.bright}${number}${colors.reset} to binary:`
      correctAnswer = this.decToBin(number)
    } else {
      const binaryNumber = this.decToBin(number)
      question = `Convert ${colors.bright}${binaryNumber}${colors.reset} to decimal:`
      correctAnswer = number.toString()
    }

    console.log(`${colors.blue}Question:${colors.reset} ${question}`)
    userAnswer = await this.askQuestion("Your answer: ")

    if (userAnswer.toLowerCase() === "quit") {
      return false
    }

    this.totalQuestions++

    if (userAnswer.trim() === correctAnswer) {
      this.score++
      console.log(`${colors.green}${colors.bright}✅ Correct!${colors.reset}`)
      if (questionType === "dec2bin") {
        console.log(`${colors.green}${number} in binary is indeed ${correctAnswer}${colors.reset}`)
      } else {
        console.log(`${colors.green}${this.decToBin(number)} in decimal is indeed ${correctAnswer}${colors.reset}`)
      }
    } else {
      console.log(`${colors.red}${colors.bright}❌ Wrong!${colors.reset}`)
      if (questionType === "dec2bin") {
        console.log(`${colors.red}${number} in binary is ${correctAnswer}, not ${userAnswer}${colors.reset}`)
      } else {
        console.log(
          `${colors.red}${this.decToBin(number)} in decimal is ${correctAnswer}, not ${userAnswer}${colors.reset}`,
        )
      }
    }

    return true
  }

  // Show final score
  async showFinalScore() {
    console.log(`\n${colors.cyan}${colors.bright}🏆 FINAL SCORE 🏆${colors.reset}`)
    console.log(`${colors.yellow}You got ${this.score} out of ${this.totalQuestions} questions correct!${colors.reset}`)

    const percentage = this.totalQuestions > 0 ? Math.round((this.score / this.totalQuestions) * 100) : 0

    if (percentage >= 90) {
      console.log(
        `${colors.green}${colors.bright}🌟 EXCELLENT! You're a binary master! (${percentage}%)${colors.reset}`,
      )
    } else if (percentage >= 70) {
      console.log(
        `${colors.blue}${colors.bright}👍 GOOD JOB! You're getting the hang of it! (${percentage}%)${colors.reset}`,
      )
    } else if (percentage >= 50) {
      console.log(
        `${colors.yellow}${colors.bright}📚 KEEP PRACTICING! You're on the right track! (${percentage}%)${colors.reset}`,
      )
    } else {
      console.log(
        `${colors.red}${colors.bright}💪 DON'T GIVE UP! Practice makes perfect! (${percentage}%)${colors.reset}`,
      )
    }

    await this.askQuestion("\nPress Enter to continue...")
  }

  // Helper method to ask questions
  askQuestion(question) {
    return new Promise((resolve) => {
      this.rl.question(question, resolve)
    })
  }

  // Helper method for delays
  delay(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms))
  }

  // Quit the game
  quit() {
    console.log(`\n${colors.cyan}${colors.bright}Thanks for playing Binary Game! 🎮${colors.reset}`)
    console.log(`${colors.yellow}Keep practicing those binary conversions! 💻${colors.reset}\n`)
    this.rl.close()
    process.exit(0)
  }

  // Start the game
  async run() {
    await this.showMenu()
  }
}

// Create and run the game
const game = new BinaryGame()

// Handle Ctrl+C gracefully
process.on("SIGINT", () => {
  console.log(`\n\n${colors.cyan}Game interrupted. Thanks for playing! 👋${colors.reset}`)
  process.exit(0)
})

// Start the game
game.run().catch(console.error)
