# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 09:35:59 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$16,120.00`
- Equity: `$31,295.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$650.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   1      5     14525.0                 15175.0        29.05          30.35       350.6        347.44     last_price_stale                        NaN                unavailable                   False           650.0                   4.48          97.3               37              0.63         45.67             0.0                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           91.67               12            1.13              2.58        325.20                26.25         0.549          pass              0.463             27.7                           0.334                0.37              0.103                                 ok            True                  False
  KLAC           85.71               35            0.58              7.36       1801.17                50.53         0.536          pass              0.521             49.4                           0.349                4.70              0.527                                 ok            True                  False
  SNPS           96.97               33            0.98              3.45        500.94                42.05         0.528          pass              0.708             34.0                           0.323               -0.00              0.038                                 ok            True                  False
  MSFT           84.00               25            0.94              2.76        420.74                29.78         0.506          pass              0.429             57.3                           0.475                1.05              0.025                                 ok            True                  False
   STX           93.10               29            1.61              8.96        791.63                57.76         0.501          pass              0.616             30.0                           0.314                5.98              0.587                                 ok            True                  False
 CMCSA           90.00               40            0.04              0.01         24.76                59.98         0.617          pass              0.807             92.9                           0.544               -8.57             -0.893 downtrend_blocked_slope_and_streak           False                  False
  SHOP           85.00               40            0.73              0.51        100.06                79.48         0.608          pass              0.570             58.7                           0.344              -21.96             -1.979 downtrend_blocked_slope_and_streak           False                  False
  INSM           42.86               14            3.41              2.61        108.02               111.34         0.605          pass              0.114              8.9                           0.202              -24.71             -2.311 downtrend_blocked_slope_and_streak           False                  False
  MELI           88.10               42            0.15              1.58       1546.13                58.33         0.557          pass              0.731             86.6                           0.551              -14.83             -2.044            downtrend_blocked_slope           False                  False
  PAYX           95.65               23            0.11              0.07         91.51                27.50         0.539          pass              0.832             97.2                           0.723                0.15             -0.105                                 ok           False                  False
  META           76.00               25            1.12              4.83        612.16                37.75         0.524          pass              0.318             55.1                           0.440               -0.50              0.046                                 ok           False                  False
   APP           83.72               43            0.16              0.58        500.75                64.32         0.522          pass              0.624             90.8                           0.578                5.30              0.367                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-05-18T03:00:02.728743-04:00   data_refresh  data_refresh                               {'saved': 92}
2026-05-16T02:55:09.369538-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:50:03.948678-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:45:01.564452-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:40:01.759045-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:35:01.904686-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:30:04.868117-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:25:04.937005-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:20:05.919345-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:15:02.185083-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518093559)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518093559)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518093559)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518093559)

</details>
