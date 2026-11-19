# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 10:20:05 EST`
Last processed slot: `manage_1030`

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

- Cash: `$100,946.30`
- Equity: `$100,946.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00400000     15          2026-11-18         2026-11-19        33.15      29.835 -4972.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   APP           92.59               27            2.03              5.57        388.52               121.61         0.771          pass              0.607             27.0                           0.218                7.54              0.351                  ok            True                  False
  IDXX           97.14               35            0.82              3.99        696.76                78.12         0.697          pass              0.783             48.7                           0.471                3.29              0.214                  ok            True                  False
  ABNB           86.21               29            1.19              1.51        179.56                55.20         0.566          pass              0.411             20.7                           0.214                4.66             -0.102                  ok            True                  False
 CMCSA           92.86               14            1.60              0.28         25.12                34.19         0.563          pass              0.473             15.6                           0.229               -0.46              0.258                  ok            True                  False
  FAST           90.00               10            1.17              0.44         53.77                20.11         0.557          pass              0.356             11.3                           0.194                0.81              0.096                  ok            True                  False
  AAPL          100.00               21            0.85              2.09        351.56                27.20         0.555          pass              0.605             25.3                           0.324                1.62              0.219                  ok            True                  False
  REGN           83.78               37            0.73              4.83        943.46                54.27         0.551          pass              0.540             67.8                           0.643                3.96              0.515                  ok            True                  False
   MAR           80.00               10            1.61              4.78        423.12                24.12         0.539          pass              0.136             27.3                           0.305                0.25              0.105                  ok            True                  False
   ROP           85.00               20            1.20              3.96        469.17                42.60         0.531          pass              0.318             21.7                           0.294               -5.24             -0.248                  ok            True                  False
   CEG           90.91               33            1.08              1.99        261.89                59.92         0.530          pass              0.497              0.0                           0.150                8.62              0.574                  ok            True                  False
  ODFL           88.24               34            0.89              1.09        174.64                43.99         0.524          pass              0.494             20.8                           0.159                1.75              0.400                  ok            True                  False
   CSX           82.35               17            1.31              0.47         51.13                35.07         0.523          pass              0.183              6.9                           0.111               -0.33              0.216                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                           detail
2026-11-19T10:20:05.689332-05:00 early_entry_1020 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "APP270115C00400000", "fill_price": 29.835, "pnl": -4972.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-19T10:15:01.694448-05:00 early_entry_1015 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:10:05.743746-05:00 early_entry_1010 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:05:05.527736-05:00 early_entry_1005 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:00:06.381004-05:00 early_entry_1000 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T00:00:05.435730-05:00     data_refresh       data_refresh                                                                                                                                                        {'saved': 91, 'empty': 2}
2026-11-18T15:10:05.947802-05:00       entry_1500       slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-11-18T15:05:06.246695-05:00       entry_1500       slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-11-18T15:00:06.306059-05:00       entry_1500       slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119102005)

</details>
