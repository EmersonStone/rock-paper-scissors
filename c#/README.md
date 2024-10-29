# Rock, Paper, Scissors (C#)

This is an implementation of a simple rock, paper, scissors app in C#.

## Requirements

- .NET SDK

You will need the .NET SDK, which includes the command-line tool `dotnet`. Here is how to install it in the terminal:

```
wget https://dot.net/v1/dotnet-install.sh
chmod +x dotnet-install.sh
./dotnet-install.sh -c 7.0
export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools
```

## Compilation

To 'compile' the source code for this application, open up a terminal, navigate
to the current directory, and run the following commands:

```
dotnet new console -o TempProject
cp rps.cs TempProject/Program.cs
```

If you do not want to copy the program into the TempProject using `cp`, you can also move it using `mv`.

## Syntax

This is a command-line application. To play, open up a terminal, navigate to
the current directory, and run the following commands after compiling:

```
cd TempProject
```

After changing into the `TempProject` directory, you can run the following command as many times as you like to run the program:

```
dotnet run
```

Once you are done running the program, if you want to remove the `TempProject` directory and all of it's contents, you can run the following commands:

```
cd ..
rm -rf TempProject
```