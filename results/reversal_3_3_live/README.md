# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 10:15:10 EDT`
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

- Cash: `$38,043.00`
- Equity: `$38,043.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score     timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   BKR           90.00               10            2.24              1.01         63.85                33.24         0.555              pass              0.379             19.1                           0.237                5.29              0.735                       ok            True                  False
  INSM           75.00               16            2.40              2.22        131.33               107.72         0.767              pass              0.119              0.9                           0.036               27.21              3.788                       ok           False                  False
  ISRG           87.50               40            0.21              0.60        401.01                69.94         0.665              pass              0.688             73.7                           0.701               13.44              1.343                       ok           False                  False
  MPWR           84.21               38            0.32              3.23       1423.63                55.33         0.573              pass              0.557             66.9                           0.402                7.92              0.620                       ok           False                  False
  FAST          100.00               27            0.21              0.08         52.19                25.01         0.567              pass              0.813             81.0                           0.763               11.68              1.209                       ok           False                  False
   HON           86.96               23            1.02              1.69        234.62                35.57         0.555              pass              0.328              0.0                           0.186               -3.71             -0.619  downtrend_blocked_slope           False                  False
   MAR           92.50               40            0.20              0.50        354.37                36.15         0.537              pass              0.656             23.1                           0.303               -5.76             -0.453  downtrend_blocked_slope           False                  False
  PCAR           97.30               37            0.41              0.38        130.90                29.70         0.499   below_threshold              0.852             74.0                           0.641               -2.42             -0.168                       ok           False                  False
  ROST           92.31               26            0.93              1.61        247.56                22.10         0.490   below_threshold              0.664             59.9                           0.620               -2.62             -0.103 downtrend_blocked_streak           False                  False
  TTWO           85.00               40            0.47              0.81        242.65                36.12         0.443   below_threshold              0.516             46.0                           0.339               -2.26              0.187                       ok           False                  False
   WMT           76.47               34            0.75              0.61        115.75                19.91         0.426   below_threshold              0.254             17.1                           0.171                3.64              0.309                       ok           False                  False
  CSCO             NaN                0            6.80              5.90        121.35                27.02           NaN no_signal_history                NaN              NaN                           0.578                1.66              0.404                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-13T10:15:10.251023-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:10:10.565177-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:05:05.347522-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:00:40.571954-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T16:10:05.737758-04:00      manage_1600               exit                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.275, "pnl": 2945.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.96, "ticker": "PYPL"}
2026-08-12T15:10:02.859897-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T15:05:01.844432-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T15:00:05.838076-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T14:55:05.864031-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T14:50:05.779182-04:00       entry_1500              entry {"allocated_cash": 17360.0, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 62, "early_entry_score": 0.819, "entry_mode": "regular", "entry_option_price": 2.8, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7246.0, "option_spread_pct": 5.71, "option_volume": 86.0, "success_rate": 93.94, "ticker": "PYPL", "timing_score": 0.657}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813101510)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813101510)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813101510)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813101510)

</details>
