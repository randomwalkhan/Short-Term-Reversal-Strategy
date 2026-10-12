# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 09:35:06 EDT`
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
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 54400.0         3.65            3.4       59.31          60.6     last_price_stale                        NaN                unavailable                   False         -4000.0                  -6.85          93.1               29              1.17         50.42             0.0                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           82.14               28            0.98              3.49        508.49                55.08         0.598            pass              0.297             20.2                           0.252               20.93              2.053                                 ok            True                  False
  CSCO           89.47               19            0.89              0.74        118.07                33.46         0.578            pass              0.439             22.8                           0.227               10.36              1.212                                 ok            True                  False
  QCOM           91.18               34            0.48              0.60        175.24                55.68         0.596            pass              0.710             64.3                           0.535               -6.84             -0.687 downtrend_blocked_slope_and_streak           False                  False
   STX           83.33               24            2.69             14.75        776.68                69.65         0.550            pass              0.268             10.1                           0.234              -17.32             -2.234            downtrend_blocked_slope           False                  False
  INTC           85.19               27            2.39              1.75        103.95                69.66         0.525            pass              0.352             15.8                           0.387              -11.92             -1.424 downtrend_blocked_slope_and_streak           False                  False
   WDC           74.07               27            2.29              6.37        394.55                64.73         0.523            pass              0.197             10.6                           0.250              -14.35             -1.829            downtrend_blocked_slope           False                  False
   XEL           85.19               27            0.32              0.16         73.70                19.01         0.517            pass              0.393             29.9                           0.268                5.36              0.575                                 ok           False                  False
  DASH           88.10               42            0.49              0.68        196.21                43.05         0.501            pass              0.634             56.0                           0.463                9.61              0.823                                 ok           False                  False
  MPWR           83.33               18            2.60             25.23       1375.48                56.07         0.495 below_threshold              0.207              5.0                           0.095                0.08              0.241                                 ok           False                  False
  ALNY           83.33               42            0.51              0.83        232.32                44.87         0.490 below_threshold              0.338              0.0                           0.200               -9.35             -1.060 downtrend_blocked_slope_and_streak           False                  False
   ADI           88.89               18            1.47              4.17        404.40                31.03         0.487 below_threshold              0.390             17.1                           0.139                1.21              0.221                                 ok           False                  False
  NXPI           88.00               25            1.11              1.76        226.76                37.45         0.483 below_threshold              0.468             35.4                           0.389               -4.79             -0.466 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012093506)

</details>
