# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 09:30:05 EDT`
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

- Cash: `$41,269.30`
- Equity: `$79,609.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$-1,755.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode        instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
    ZS     option         option ZS261120C00200000       2026-10-02                   1     27     40095.0                 38340.0        14.85           14.2      196.86         197.8     last_price_stale                        NaN                unavailable                   False         -1755.0                  -4.38         94.59               37              0.97         55.98            0.78                   77.3                 818.0          103.0               0.04                      ok
```

## Today's Closed Trades (2026-10-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           84.85               33            1.38              1.58        162.99               114.85         0.740          pass              0.504             49.2                           0.550               13.80              0.986                                 ok            True                  False
  AMGN           83.87               31            0.54              1.51        402.39                47.11         0.561          pass              0.480             60.3                           0.394                1.96              0.119                                 ok            True                  False
   TRI           87.50               32            0.96              0.66         97.34                53.36         0.552          pass              0.408              2.1                           0.178                1.31              0.077                                 ok            True                  False
  ASML           81.25               32            0.67              8.76       1863.56                42.39         0.547          pass              0.415             60.0                           0.592                8.38              0.842                                 ok            True                  False
  DRAM           80.56               36            0.11              0.05         61.72                54.09         0.586          pass              0.487             80.0                           0.626                0.15             -0.114                                 ok           False                  False
  TEAM          100.00               42            0.07              0.10        187.85                53.33         0.565          pass              0.936             93.1                           0.586               -4.05             -0.465           downtrend_blocked_streak           False                  False
  CRWD           89.13               46            0.01              0.03        270.03                56.43         0.557          pass              0.795             98.6                           0.596                8.28              0.751                                 ok           False                  False
  QCOM           92.68               41            0.06              0.08        184.83                56.36         0.551          pass              0.870             92.4                           0.431               -4.88             -0.882 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           92.86               14            0.64              0.26         58.08                14.86         0.543          pass              0.479             18.5                           0.247               -3.06             -0.521 downtrend_blocked_slope_and_streak           False                  False
  PANW           82.22               45            0.38              1.08        402.78                54.74         0.532          pass              0.469             52.3                           0.405                8.05              0.707                                 ok           False                  False
  LRCX           81.40               43            0.43              1.04        347.04                57.64         0.527          pass              0.491             67.2                           0.621               14.59              1.450                                 ok           False                  False
  INTC           79.17               24            3.01              2.52        118.25                74.20         0.527          pass              0.257             37.1                           0.485               -4.97             -0.584            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-05T03:00:05.114767-04:00   data_refresh  data_refresh                   {'saved': 92, 'empty': 1}
2026-10-03T02:55:05.889514-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:50:05.063422-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:45:04.071042-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:40:05.983879-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:35:05.098506-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:30:06.414009-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:25:01.959731-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:20:06.968956-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:15:04.972202-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005093005)

</details>
