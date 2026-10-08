# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 10:40:05 EDT`
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

- Cash: `$108,579.30`
- Equity: `$108,579.30`
- Realized PnL: `$98,579.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0  -10.000000        stop_loss_hit_at_scan
  ABNB     option         option ABNB261120C00160000     55          2026-10-06         2026-10-08        9.475     11.0500  8662.5   16.622691 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.48               27            3.84              4.28        157.08               112.38         0.604          pass              0.367             51.2                           0.785                4.42              1.058                                 ok            True                  False
  MPWR           88.00               25            1.60             15.96       1419.14                55.22         0.571          pass              0.520             49.8                           0.654                5.22              0.852                                 ok            True                  False
  CSCO           88.89               27            0.56              0.46        117.19                34.80         0.560          pass              0.563             52.2                           0.498                9.55              1.204                                 ok            True                  False
  MSTR           91.89               37            0.67              0.72        153.06                80.80         0.632          pass              0.805             81.6                           0.861               -5.74             -0.114           downtrend_blocked_streak           False                  False
  QCOM           87.50               24            1.72              2.13        176.21                56.66         0.583          pass              0.453             33.8                           0.504              -10.39             -1.100 downtrend_blocked_slope_and_streak           False                  False
   WDC           82.22               45            0.07              0.20        405.33                65.89         0.545          pass              0.604             96.7                           0.769              -10.03             -1.311            downtrend_blocked_slope           False                  False
   STX           86.67               30            2.01             11.35        802.70                69.74         0.539          pass              0.466             33.6                           0.343              -12.65             -1.571            downtrend_blocked_slope           False                  False
 CMCSA           88.89               18            0.31              0.05         20.92                21.76         0.532          pass              0.544             66.7                           0.456               -4.20             -0.343            downtrend_blocked_slope           False                  False
  INTC           84.62               26            2.55              2.02        112.26                69.90         0.524          pass              0.393             37.0                           0.619              -13.46             -1.049 downtrend_blocked_slope_and_streak           False                  False
  REGN           83.33                6            2.14             11.12        737.36                27.38         0.521          pass              0.183             14.0                           0.219               -8.77             -0.772            downtrend_blocked_slope           False                  False
  LRCX           81.40               43            0.07              0.16        329.44                55.85         0.509          pass              0.582             98.0                           0.909                7.20              0.811                                 ok           False                  False
  GILD           84.62               13            1.27              1.31        146.29                18.65         0.509          pass              0.240             15.2                           0.156               -3.14             -0.500 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-10-08T10:40:05.011138-04:00 early_entry_1040 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:35:07.119041-04:00 early_entry_1035 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:35:07.119041-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "ABNB261120C00160000", "fill_price": 11.05, "pnl": 8662.5, "reason": "take_profit_day2_hit_at_scan", "return_pct": 16.62, "ticker": "ABNB"}
2026-10-08T10:30:06.096812-04:00 early_entry_1030 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:25:06.880454-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:20:05.114713-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:15:04.991008-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:10:05.110275-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:05:06.592020-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:00:03.810887-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008104005)

</details>
