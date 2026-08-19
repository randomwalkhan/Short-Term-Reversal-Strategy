# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-19 09:37:24 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$53,138.00`
- Equity: `$53,138.00`
- Realized PnL: `$43,138.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           83.78               37            1.55              1.40        128.37               165.44         0.809          pass              0.560             66.2                           0.404               -9.24              0.039                      ok            True                  False
   WDC           81.48               27            2.01              6.97        493.17               104.27         0.628          pass              0.331             38.3                           0.270              -11.37             -0.055                      ok            True                  False
  LRCX           85.71               28            2.39              5.49        325.57                86.42         0.615          pass              0.375             13.6                           0.188                0.73              0.659                      ok            True                  False
  KLAC           80.00               30            1.49              2.03        193.92                69.46         0.586          pass              0.237             15.0                           0.255               -1.71              0.351                      ok            True                  False
   STX           88.46               26            1.92             12.13        898.48                83.43         0.580          pass              0.496             35.3                           0.263                4.85              1.327                      ok            True                  False
  ASML           87.10               31            1.02             12.93       1797.44                47.17         0.565          pass              0.472             28.6                           0.239                4.24              0.842                      ok            True                  False
  INTC           85.71               35            2.39              1.62         95.99                81.46         0.534          pass              0.413             13.5                           0.204               -6.43             -0.238                      ok            True                  False
    MU           83.78               37            0.38              2.48        939.70               104.10         0.709          pass              0.609             85.7                           0.435                4.99              0.988                      ok           False                  False
  AMAT           89.29               28            1.69              6.07        511.73                84.57         0.653          pass              0.442              3.1                           0.254               -7.49             -0.609 downtrend_blocked_slope           False                  False
   HON           88.00               25            0.57              0.91        227.32                37.29         0.591          pass              0.494             40.4                           0.483               -8.72             -0.903 downtrend_blocked_slope           False                  False
  NXPI           74.36               39            0.01              0.02        228.55                51.36         0.569          pass              0.545             98.2                           0.564               -3.82             -0.277 downtrend_blocked_slope           False                  False
  META           88.10               42            0.32              1.23        543.14                50.80         0.553          pass              0.689             72.6                           0.581               -7.83             -0.635 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-08-18T12:30:08.738941-04:00      manage_1230               exit {"asset_type": "option", "contract_symbol": "ALNY260918C00220000", "fill_price": 17.8, "pnl": 6240.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.06, "ticker": "ALNY"}
2026-08-18T11:46:30.861767-04:00 early_entry_1145 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:55:01.557589-04:00 early_entry_1055 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:35:03.185404-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:33:08.530330-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T09:38:41.008763-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-18T09:20:07.104993-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-18T09:15:08.426968-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-18T09:11:00.046303-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-18T08:52:52.256088-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260819093724)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260819093724)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260819093724)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260819093724)

</details>
