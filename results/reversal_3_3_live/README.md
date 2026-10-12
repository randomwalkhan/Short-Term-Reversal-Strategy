# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 09:30:05 EDT`
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

- Cash: `$58,874.30`
- Equity: `$113,274.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$-4,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 54400.0         3.65            3.4       59.31         59.83     last_price_stale                        NaN                unavailable                   False         -4000.0                  -6.85          93.1               29              1.17         50.42            0.05                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           91.43               35            0.98              1.06        153.89                79.86         0.625            pass              0.534              0.0                           0.177               -2.75             -0.221                                 ok            True                  False
  MPWR           83.33               18            2.46             23.85       1376.07                56.07         0.505            pass              0.193              0.0                           0.179                0.22              0.247                                 ok            True                  False
  DASH           87.80               41            0.62              0.85        196.13                43.05         0.500            pass              0.569             36.8                           0.308                9.47              0.818                                 ok            True                  False
  QCOM           88.46               26            1.21              1.49        174.86                55.68         0.599            pass              0.392              0.0                           0.258               -7.52             -0.721 downtrend_blocked_slope_and_streak           False                  False
   STX           84.00               25            2.55             14.00        777.00                69.65         0.556            pass              0.262              0.0                           0.214              -17.20             -2.228            downtrend_blocked_slope           False                  False
  CSCO           93.94               33            0.26              0.22        118.30                33.46         0.546            pass              0.580              0.0                           0.182               11.05              1.240                                 ok           False                  False
  INTC           84.00               25            2.41              1.76        103.94                69.66         0.538            pass              0.260              0.0                           0.255              -11.94             -1.425 downtrend_blocked_slope_and_streak           False                  False
   WDC           74.07               27            2.37              6.59        394.45                64.73         0.519            pass              0.178              4.1                           0.271              -14.42             -1.832            downtrend_blocked_slope           False                  False
  MCHP           96.30               27            1.32              0.70         75.25                38.98         0.490 below_threshold              0.562              0.0                           0.183               -4.38             -0.448            downtrend_blocked_slope           False                  False
   ADI           93.10               29            0.72              2.04        405.32                31.03         0.477 below_threshold              0.524              0.0                           0.200                1.98              0.256                                 ok           False                  False
   KHC           90.91               33            0.20              0.03         22.26                19.43         0.469 below_threshold              0.566             25.0                           0.469               -5.67             -0.528 downtrend_blocked_slope_and_streak           False                  False
  AVGO           88.89               36            0.52              1.32        360.98                38.10         0.467 below_threshold              0.597             46.7                           0.426                2.89              0.481                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-12T03:00:05.508504-04:00   data_refresh  data_refresh                   {'saved': 90, 'empty': 3}
2026-10-10T02:55:05.468213-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:50:06.073538-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:45:04.438965-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:40:05.495022-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:35:05.586025-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:30:06.510407-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:25:06.103095-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:20:06.276038-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:15:05.578825-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012093005)

</details>
