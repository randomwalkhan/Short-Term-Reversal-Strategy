# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-18 09:38:41 EDT`
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

- Cash: `$24,658.00`
- Equity: `$47,218.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$320.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   1     16     22240.0                 22560.0         13.9           14.1      224.68        222.73     last_price_stale                        NaN                unavailable                   False           320.0                   1.44         84.62               26              1.73         43.62             0.0                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ALNY           87.18               39            0.83              1.31        224.04               127.60         0.812          pass              0.644             59.2                           0.383                1.70              0.229                                 ok            True                  False
  INSM           85.00               40            0.63              0.57        128.08               109.50         0.756          pass              0.525             38.6                           0.239               29.12              1.810                                 ok            True                  False
    MU           83.33               24            3.96             28.03        999.74               104.10         0.604          pass              0.329             28.9                           0.568                8.85              1.152                                 ok            True                  False
  UPRO           85.00               20            1.47              1.59        153.72                41.29         0.582          pass              0.327             22.9                           0.333               -1.30              0.017                                 ok            True                  False
  QCOM           82.93               41            0.63              0.72        161.87                49.62         0.509          pass              0.563             77.9                           0.819               -0.93              0.100                                 ok            True                  False
  NVDA           89.29               28            1.69              2.67        223.87                39.09         0.506          pass              0.513             31.7                           0.476                4.37              0.342                                 ok            True                  False
   WDC           90.00               20            5.05             18.94        527.89               104.27         0.501          pass              0.502             39.7                           0.531               -7.22              0.153                                 ok            True                  False
  SHOP           97.62               42            0.16              0.17        148.58                85.84         0.695          pass              0.945             92.0                           0.584               20.36              1.124                                 ok           False                  False
  AMZN           78.79               33            0.80              1.46        260.68                61.74         0.630          pass              0.339             41.0                           0.336               -6.56             -0.690 downtrend_blocked_slope_and_streak           False                  False
   HON           88.00               25            0.63              1.01        229.01                37.29         0.571          pass              0.400              9.9                           0.148               -8.08             -0.871            downtrend_blocked_slope           False                  False
   KHC           84.38               32            0.06              0.01         24.75                37.82         0.568          pass              0.538             72.7                           0.502               -7.15             -0.431            downtrend_blocked_slope           False                  False
  PCAR          100.00               23            1.10              1.01        130.41                28.21         0.542          pass              0.541              0.0                           0.181               -4.57             -0.358            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-08-18T09:38:41.008763-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T09:20:07.104993-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T09:15:08.426968-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T09:11:00.046303-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:52:52.256088-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:35:07.917262-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:32:57.454440-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:15:02.899134-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:12:27.971020-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T07:55:02.255122-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260818093841)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260818093841)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260818093841)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260818093841)

</details>
