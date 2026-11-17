# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 10:10:04 EST`
Last processed slot: `manage_1000`

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

- Cash: `$111,239.80`
- Equity: `$111,239.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   APP           92.31               13            3.28              9.53        411.14               119.50         0.801          pass              0.436              2.5                           0.064               63.58              4.157                                 ok            True                  False
  FTNT           81.58               38            1.01              0.88        122.89                92.89         0.673          pass              0.392             32.1                           0.199               -4.75             -0.097                                 ok            True                  False
  QCOM           83.33               24            1.91              2.25        167.56                68.75         0.585          pass              0.241              0.0                           0.163                0.53              0.337                                 ok            True                  False
   CSX           80.95               21            1.04              0.38         51.87                34.26         0.572          pass              0.209             17.6                           0.206                1.52              0.275                                 ok            True                  False
   CEG           90.62               32            1.34              2.61        276.70                60.48         0.566          pass              0.580             31.1                           0.229                4.22              1.284                                 ok            True                  False
   ADP           86.36               22            0.96              2.10        312.53                28.40         0.549          pass              0.419             38.1                           0.533                4.87              0.397                                 ok            True                  False
  META           81.82               33            0.62              2.74        625.24                41.97         0.529          pass              0.415             53.4                           0.592                0.24              0.172                                 ok            True                  False
  BKNG           80.49               41            0.68              0.75        157.21                49.20         0.501          pass              0.390             42.4                           0.362                0.51             -0.439                                 ok            True                  False
  SOXL           69.70               33            1.08              0.37         48.60               265.45         0.952          pass              0.472             74.6                           0.359              -34.03             -1.268 downtrend_blocked_slope_and_streak           False                  False
  INTC           67.86               28            2.20              0.86         55.08               143.34         0.812          pass              0.337             45.3                           0.387              -10.45             -0.120           downtrend_blocked_streak           False                  False
  ALNY           76.47               34            1.35              1.50        159.09               110.59         0.741          pass              0.340             35.1                           0.289               -1.44              0.072                                 ok           False                  False
  LRCX           68.29               41            0.15              0.22        210.73               105.03         0.720          pass              0.540             89.4                           0.431               -8.76              0.285           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-17T10:10:04.914368-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:05:06.251834-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:00:06.465677-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T09:50:06.673535-05:00      manage_1000               exit                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "QCOM261218C00170000", "fill_price": 10.0125, "pnl": -5785.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "QCOM"}
2026-11-17T00:00:04.730535-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-11-16T15:10:06.484281-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:05:04.471128-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:00:02.614277-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:55:05.526400-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:50:05.632368-05:00       entry_1500              entry {"allocated_cash": 57850.0, "asset_type": "option", "contract_symbol": "QCOM261218C00170000", "contracts": 52, "early_entry_score": 0.463, "entry_mode": "regular", "entry_option_price": 11.125, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 2.25, "option_volume": 163.0, "success_rate": 85.19, "ticker": "QCOM", "timing_score": 0.599}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117101004)

</details>
