<?php

namespace App\Services;

use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Illuminate\Support\Facades\Log;

class ScriptRunner
{
    public function runScript(string $scriptPath, array $arguments = [], string $command = null)
    {
        $full_command = [$command ?? (env('BASE_COMMAND') ?? 'python3'), $scriptPath];

        foreach ($arguments as $name => $value) {
            $full_command[] = '--' . $name;
            $full_command[] = $value;
        }

        Log::info('Full Command:', $full_command);
        Log::info('Python Script Started...');

        $process = new Process($full_command);
        $process->setWorkingDirectory('/home/office/Code/extern_component_editor/micro_service/test_runner/playwright');
        $process->setTimeout(null);

        // Use run() method instead of start()
        $process->run();

        // Optionally, retrieve output or handle errors after completion
        if (!$process->isSuccessful()) {
            Log::info("Error: ", $process->getOutput());
            throw new ProcessFailedException($process);
        }

        Log::info('Python Script Finished.');
        Log::info('Output: ' . $process->getOutput());

        return $process;
    }
}
