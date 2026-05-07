# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-07 15:55:05 EDT`
Last processed slot: `manage_1600`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$14,483.50`
- Equity: `$27,333.50`
- Realized PnL: `$17,583.50`
- Unrealized PnL: `$-250.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260618C00290000       2026-05-07                   0     10     13100.0                 12850.0         13.1          12.85      283.62        285.21          -250.0                  -1.91         91.67               12              2.01         41.87           39.01                  67.07                1293.0          214.0               0.05                      ok
```

## Today's Closed Trades (2026-05-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CRWD     option         option CRWD260618C00470000      3          2026-05-06         2026-05-07       33.025       51.55 5557.5   56.093868 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
   TXN           89.47               19            1.46              2.96        288.17                67.07         0.678          pass                1.57              0.520                                 ok            True
  INTC          100.00               20            3.00              2.37        111.99                95.68         0.662          pass               64.15              4.326                                 ok            True
  FAST           96.00               25            0.79              0.25         44.60                34.69         0.556          pass               -1.89             -0.076                                 ok            True
  SBUX          100.00               10            2.18              1.62        105.74                31.94         0.554          pass                4.60              0.812                                 ok            True
  MDLZ           82.61               23            0.75              0.33         61.73                24.46         0.519          pass                6.40              0.814                                 ok            True
  ASML           80.77               26            1.73             18.72       1536.72                46.11         0.510          pass                7.30              0.582                                 ok            True
 CMCSA           88.89               18            0.81              0.15         26.38                61.67         0.710          pass              -17.11             -1.134 downtrend_blocked_slope_and_streak           False
  NXPI           66.67                3            4.32              9.18        299.62                84.51         0.639          pass               20.43              2.654                                 ok           False
  GEHC           73.68               38            0.54              0.23         61.63                55.11         0.560          pass              -12.15             -1.564            downtrend_blocked_slope           False
   CSX           83.33                6            2.60              0.83         45.22                28.34         0.530          pass               -3.88             -0.203                                 ok           False
  ROST          100.00                6            2.07              3.32        227.49                15.20         0.514          pass               -1.21              0.019                                 ok           False
   KDP           87.88               33            0.19              0.04         28.54                34.76         0.512          pass               -0.09             -0.003                                 ok           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                         detail
2026-05-07T15:55:05.013610-04:00 manage_1600 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:40:04.301487-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:35:09.139839-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:30:09.012076-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:25:04.977816-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:10:07.636776-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:05:07.086274-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:00:07.624219-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T14:55:04.902714-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T14:50:57.198065-04:00  entry_1500        entry {"allocated_cash": 13100.0, "asset_type": "option", "contract_symbol": "TXN260618C00290000", "contracts": 10, "entry_option_price": 13.1, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 1293.0, "option_spread_pct": 4.58, "option_volume": 214.0, "success_rate": 91.67, "ticker": "TXN", "timing_score": 0.69}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507155505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507155505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507155505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507155505)

</details>
