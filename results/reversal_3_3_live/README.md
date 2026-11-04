# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 10:20:05 EST`
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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           75.00               32            1.67              0.71         60.25               129.60         0.769            pass              0.404             60.1                           0.655              -35.96             -4.890            downtrend_blocked_slope           False                  False
  SOXL           72.41               29            1.90              0.97         72.70               167.58         0.754            pass              0.431             76.3                           0.686              -30.52             -2.913            downtrend_blocked_slope           False                  False
  DRAM           73.08               26            1.36              0.45         47.45                69.30         0.600            pass              0.355             62.9                           0.578               -4.41             -0.086                                 ok           False                  False
  REGN           88.89                9            2.17             14.81        967.01                48.26         0.576            pass              0.295              0.0                           0.157               18.19              2.126                                 ok           False                  False
  AVGO           78.38               37            0.30              0.70        331.83                44.04         0.514            pass              0.486             84.9                           0.568               -1.97              0.003                                 ok           False                  False
  ASML           75.00               16            2.11             22.92       1542.32                44.05         0.513            pass              0.194             34.3                           0.506               -9.26             -0.538            downtrend_blocked_slope           False                  False
  KLAC           72.50               40            0.34              0.37        156.04                57.09         0.511            pass              0.512             86.9                           0.742               -4.75              0.297                                 ok           False                  False
  AMAT           70.00               40            0.41              1.09        381.45                58.39         0.505            pass              0.513             87.6                           0.813               -6.99             -0.219                                 ok           False                  False
  NVDA           76.00               25            0.71              1.03        206.25                32.59         0.498 below_threshold              0.373             74.5                           0.694               -7.54             -0.686 downtrend_blocked_slope_and_streak           False                  False
    MU           75.00               20            2.69             16.12        848.19                64.24         0.494 below_threshold              0.234             39.4                           0.336               -8.93             -0.605            downtrend_blocked_slope           False                  False
  MPWR           60.87               23            1.94             18.01       1320.58                60.85         0.493 below_threshold              0.260             41.3                           0.358                1.50              0.831                                 ok           False                  False
  INSM           82.98               47            0.45              0.33        104.30                60.46         0.488 below_threshold              0.328              0.0                           0.170               10.56              1.715                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-11-04T10:20:05.681556-05:00 early_entry_1020 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:15:05.290161-05:00 early_entry_1015 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:10:06.483796-05:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:05:05.606953-05:00 early_entry_1005 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:00:05.152440-05:00 early_entry_1000 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T09:20:05.283761-05:00     data_refresh       data_refresh                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-11-03T16:10:06.665587-05:00      manage_1600               exit {"asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "fill_price": 1.305, "pnl": -6815.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-03T15:10:05.032509-05:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-11-03T15:05:04.979432-05:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-11-03T15:00:05.978517-05:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104102005)

</details>
