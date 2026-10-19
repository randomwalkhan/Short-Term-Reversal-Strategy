# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 10:15:09 EDT`
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

- Cash: `$131,531.80`
- Equity: `$131,531.80`
- Realized PnL: `$121,531.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     35          2026-10-16         2026-10-19        17.05       19.65 9100.0   15.249267 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.71               21            1.87              3.55        269.85                59.14         0.547            pass              0.368             29.2                           0.253               -0.49             -0.668                                 ok            True                  False
   XEL           82.35               17            0.81              0.43         76.12                16.32         0.526            pass              0.176              4.6                           0.166                5.87              0.593                                 ok            True                  False
   ADP           92.86               28            0.57              1.15        288.41                21.32         0.511            pass              0.713             66.5                           0.499               10.37              1.094                                 ok            True                  False
  CTSH           94.44               36            0.74              0.34         65.88                41.45         0.510            pass              0.721             37.2                           0.361               12.67              1.555                                 ok            True                  False
  CTAS           91.67               24            0.98              1.46        213.06                23.07         0.510            pass              0.524             22.7                           0.218                8.29              0.972                                 ok            True                  False
   KHC           88.46               26            0.78              0.13         23.62                22.28         0.502            pass              0.524             47.1                           0.603                7.58              0.776                                 ok            True                  False
  INTU           85.71               21            1.68              3.81        323.52                39.88         0.500 below_threshold              0.349             24.5                           0.326               12.83              1.318                                 ok            True                  False
  TMUS           85.29               34            0.51              0.57        158.86                56.39         0.611            pass              0.510             49.4                           0.504               -3.86             -0.629            downtrend_blocked_slope           False                  False
   KDP           96.15               26            0.48              0.12         34.57                30.61         0.562            pass              0.788             75.0                           0.695               11.54              1.320                                 ok           False                  False
  PAYX           75.00               28            1.06              0.83        111.28                41.41         0.559            pass              0.228             17.5                           0.269               10.69              1.149                                 ok           False                  False
 CMCSA           88.89                9            1.27              0.20         21.82                21.89         0.554            pass              0.346             18.0                           0.172                1.80              0.296                                 ok           False                  False
  META           85.71               14            1.55              7.68        706.03                56.19         0.524            pass              0.319             29.0                           0.257               -5.87             -0.270 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-10-19T10:15:09.644271-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:10:06.129033-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:05:07.192059-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:00:05.134811-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T09:50:04.852472-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 19.65, "pnl": 9100.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.25, "ticker": "CEG"}
2026-10-19T03:00:04.169170-04:00     data_refresh       data_refresh                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-10-17T02:55:05.454730-04:00   share_ext_0255      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:50:06.805476-04:00   share_ext_0250      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:45:05.931268-04:00   share_ext_0245      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:40:05.272709-04:00   share_ext_0240      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019101509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019101509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019101509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019101509)

</details>
