<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\ScriptRunner;

class ScriptStatusController extends Controller
{
    protected $scriptRunner;

    public function __construct(ScriptRunner $scriptRunner)
    {
        $this->scriptRunner = $scriptRunner;
    }
    public function handle(Request $request)
    {
        $pid = $request->get('pid');
        $isRunning = $this->scriptRunner->isRunning($pid);
        $output = $this->scriptRunner->getOutput($pid);
        $all = $this->scriptRunner->getAllProcesses();

        return response()->json([
            'isRunning' => $isRunning,
            'output' => $output,
            'all' => $all
        ]);

    }
}
