<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Jobs\RunScriptJob;

class ScriptRunnerController extends Controller
{
    public function handle(Request $request)
    {
        $request->validate([
            'script_path' => 'required|string',
            'args' => 'required|array',
        ]);

        $scriptPath = $request->input('script_path');
        $arguments = $request->input('args');

        $currentWorkingDirectory = getcwd();

        $fullScriptPath = $currentWorkingDirectory . DIRECTORY_SEPARATOR . '..'.DIRECTORY_SEPARATOR.'..' .DIRECTORY_SEPARATOR  . $scriptPath;

        \Log::info('Dispatching script with arguments: ', $arguments);

        RunScriptJob::dispatch($fullScriptPath, $arguments);

        return response()->json(['message' => 'Script executed successfully'], 201);
    }
}
