# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 15:00:02 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$17,608.25`
- Equity: `$34,483.25`
- Realized PnL: `$24,370.75`
- Unrealized PnL: `$112.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260918C00100000       2026-08-06                   0     15     16762.5                 16875.0        11.18          11.25      100.37        100.42          bid_ask_mid                      11.25                bid_ask_mid                    True           112.5                   0.67          85.0               40              0.68         79.69           79.13                  86.71               28020.0         1406.0               0.03                      ok
```

## Today's Closed Trades (2026-08-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     55          2026-08-05         2026-08-06        2.865       3.325 2530.0   16.055846 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           85.00               40            0.68              0.48        100.85                86.71         0.565            pass              0.652             87.4                           0.581                0.14              0.780                                 ok            True                  False
  MNST           88.89               18            0.88              0.58         94.21                25.70         0.559            pass              0.495             49.7                           0.675                0.07             -0.080                                 ok            True                  False
  WDAY           81.25               32            1.34              1.60        169.95                67.74         0.548            pass              0.444             69.9                           0.513               31.66              2.517                                 ok            True                  False
  AMGN          100.00               20            1.19              3.39        406.38                30.87         0.500 below_threshold              0.598             27.0                           0.524                8.48              0.690                                 ok            True                  False
    MU           80.56               36            0.09              0.57        892.94               111.75         0.701            pass              0.555             98.8                           0.626               -9.88             -0.489           downtrend_blocked_streak           False                  False
  ALNY           50.00                4            4.84              7.75        225.40               127.65         0.690            pass              0.083              4.6                           0.129              -19.01             -3.032            downtrend_blocked_slope           False                  False
  ISRG           86.84               38            0.33              0.88        374.82                72.98         0.678            pass              0.629             63.9                           0.353               12.63              1.079                                 ok           False                  False
  AMAT           91.67               36            0.70              2.63        533.11                86.87         0.661            pass              0.802             83.8                           0.640               -5.74              0.160           downtrend_blocked_streak           False                  False
   ROP           93.94               33            0.43              1.19        394.02                46.42         0.588            pass              0.778             64.7                           0.515               10.62              0.816                                 ok           False                  False
  AMZN           82.61               46            0.30              0.58        272.40                61.64         0.567            pass              0.466             46.4                           0.461               16.33              2.309                                 ok           False                  False
   CSX           92.00               25            0.60              0.21         51.03                29.11         0.552            pass              0.541             21.8                           0.236               -3.78             -0.406 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                4            2.45              0.44         25.54                34.35         0.541            pass              0.581             42.2                           0.561               -1.03             -0.115                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-06T15:00:02.209761-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T14:55:01.108594-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T14:50:04.202564-04:00       entry_1500              entry {"allocated_cash": 16762.5, "asset_type": "option", "contract_symbol": "INTC260918C00100000", "contracts": 15, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 11.175, "execution_mode": "option", "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 28020.0, "option_spread_pct": 3.13, "option_volume": 1406.0, "success_rate": 85.0, "ticker": "INTC", "timing_score": 0.565}
2026-08-06T14:50:04.202564-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-06", "training_samples": 5584, "window": 5}
2026-08-06T12:00:02.173564-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:55:01.207054-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:50:03.918933-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:50:03.918933-04:00      manage_1200               exit                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.325, "pnl": 2530.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.06, "ticker": "PYPL"}
2026-08-06T11:45:03.120724-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:40:04.059152-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806150002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806150002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806150002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806150002)

</details>
