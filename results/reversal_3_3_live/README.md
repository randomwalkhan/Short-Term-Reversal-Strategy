# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 10:45:04 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261016C00130000     30          2026-09-10         2026-09-11       11.525       13.65 6375.0   18.438178 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           84.38               32            1.81              2.65        207.73                89.85         0.640            pass              0.345              6.0                           0.171              -10.04             -0.933            downtrend_blocked_slope           False                  False
  AMGN          100.00               18            1.00              2.68        381.32                44.93         0.635            pass              0.543              8.8                           0.142              -13.35             -1.563 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.91               22            0.05              0.05        136.63                17.04         0.560            pass              0.663             78.8                           0.445               -1.20             -0.182                                 ok           False                  False
    ZS           97.78               45            0.01              0.01        163.48                64.41         0.553            pass              0.954             99.6                           0.527              -12.72             -1.588            downtrend_blocked_slope           False                  False
    MU           87.50               40            0.19              1.30        976.85                56.22         0.549            pass              0.699             81.5                           0.487                4.29              0.732                                 ok           False                  False
   EXC           94.44               18            0.32              0.10         43.35                15.10         0.546            pass              0.683             63.2                           0.297               -0.68              0.007                                 ok           False                  False
  TEAM           94.74               38            0.82              1.03        179.13                63.98         0.540            pass              0.777             47.7                           0.495               -4.05             -0.733            downtrend_blocked_slope           False                  False
  ADBE           97.44               39            0.01              0.01        248.82                48.95         0.535            pass              0.946             99.8                           0.888              -13.95             -1.874 downtrend_blocked_slope_and_streak           False                  False
  PANW           66.67               24            2.51              5.96        335.94                67.54         0.522            pass              0.166              6.8                           0.159              -13.81             -1.490            downtrend_blocked_slope           False                  False
  LRCX           83.33               42            0.16              0.33        297.87                53.83         0.520            pass              0.598             85.8                           0.509               -6.60              0.008           downtrend_blocked_streak           False                  False
  ADSK           90.70               43            0.15              0.22        211.52                52.16         0.513            pass              0.800             87.9                           0.453              -21.91             -2.869 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               22            1.15              6.41        790.51                28.70         0.500 below_threshold              0.605             25.1                           0.292               -2.92             -0.166           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-09-11T10:45:04.814010-04:00 early_entry_1045 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:40:06.630614-04:00 early_entry_1040 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:35:04.843069-04:00 early_entry_1035 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:30:01.845613-04:00 early_entry_1030 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:25:04.822765-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:20:04.731608-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:15:01.602754-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:10:01.770369-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261016C00130000", "fill_price": 13.65, "pnl": 6375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.44, "ticker": "MSTR"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911104504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911104504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911104504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911104504)

</details>
