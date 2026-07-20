# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 10:15:03 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$31,411.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           84.00               25            1.01              0.40         56.39                61.55         0.642          pass              0.437             55.5                           0.670               24.17              2.813                      ok            True                  False
   WBD           87.50               16            0.69              0.13         26.81                20.40         0.575          pass              0.413             38.3                           0.324                2.16              0.390                      ok            True                  False
  PAYX          100.00               21            1.24              0.99        113.97                33.31         0.549          pass              0.594             21.8                           0.325                7.20              0.801                      ok            True                  False
   ROP           90.48               21            1.35              3.43        361.67                31.85         0.527          pass              0.524             39.5                           0.483               -1.40             -0.053                      ok            True                  False
   ADP           95.24               21            1.15              2.05        254.39                34.14         0.522          pass              0.619             31.3                           0.315                5.37              0.607                      ok            True                  False
  BKNG           83.33               24            1.32              1.68        180.96                41.44         0.518          pass              0.367             44.4                           0.340               -0.97              0.163                      ok            True                  False
  ORLY           82.76               29            1.16              0.70         85.75                41.23         0.514          pass              0.350             32.9                           0.292                0.96              0.001                      ok            True                  False
  TEAM           85.00               40            0.74              0.48         93.08                69.60         0.512          pass              0.635             83.4                           0.771                8.30              0.794                      ok            True                  False
  AAPL          100.00                5            2.02              4.71        331.72                36.42         0.629          pass              0.463              0.0                           0.150                4.59              0.695                      ok           False                  False
  MDLZ          100.00                8            1.25              0.53         60.77                32.63         0.608          pass              0.531             23.2                           0.313                1.81              0.228                      ok           False                  False
   PEP           86.36               22            0.44              0.43        136.94                30.73         0.584          pass              0.469             53.8                           0.452               -4.73             -0.528 downtrend_blocked_slope           False                  False
 CMCSA           69.23               13            0.84              0.14         23.73                29.10         0.565          pass              0.234             52.4                           0.621                0.90              0.200                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-20T10:15:03.125789-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "TXN260821C00290000", "fill_price": 23.275, "pnl": 2187.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.51, "ticker": "TXN"}
2026-07-20T10:05:02.132166-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:00:05.019489-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T03:00:02.156318-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-07-18T02:55:03.939140-04:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:50:01.103428-04:00   share_ext_0250      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:45:05.126153-04:00   share_ext_0245      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:40:02.148173-04:00   share_ext_0240      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720101503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720101503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720101503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720101503)

</details>
