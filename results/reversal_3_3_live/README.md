# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 09:30:02 EDT`
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

- Cash: `$18,164.25`
- Equity: `$32,264.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14100.0        35.25          35.25      477.34        477.01     last_price_stale                        NaN                unavailable                   False             0.0                    0.0         97.22               36              0.69         45.69             0.0                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           95.24               21            3.68              5.77        221.59               138.67         0.657          pass              0.580             13.8                           0.155               31.45              4.364                  ok            True                  False
  ROST           93.33               15            1.52              2.47        230.67                40.27         0.594          pass              0.548             33.3                           0.244                7.26              1.035                  ok            True                  False
  ASML           93.33               30            1.09             12.28       1607.49                52.38         0.569          pass              0.663             39.0                           0.355                6.22              0.944                  ok            True                  False
  AMAT           88.89               27            1.10              3.47        448.57                49.82         0.551          pass              0.541             45.3                           0.359                2.07              0.829                  ok            True                  False
  KLAC           86.96               23            1.81             24.30       1911.30                50.27         0.523          pass              0.324              0.0                           0.203                4.72              1.017                  ok            True                  False
   TXN          100.00               16            1.71              3.67        304.11                35.97         0.511          pass              0.623             44.0                           0.350               -0.76              0.298                  ok            True                  False
  UPRO           93.94               33            0.61              0.64        148.84                29.01         0.510          pass              0.591              5.1                           0.063                6.06              0.827                  ok            True                  False
  NXPI           91.67               24            1.46              3.28        319.94                48.19         0.510          pass              0.534             26.1                           0.323                8.63              1.248                  ok            True                  False
  FAST           93.33               15            1.40              0.43         44.01                16.05         0.503          pass              0.439              0.0                           0.263                0.74              0.189                  ok            True                  False
  INSM           73.68               38            0.83              0.62        106.64               110.85         0.764          pass              0.263              0.0                           0.240               -2.86             -0.147                  ok           False                  False
   TRI           79.17               24            0.25              0.15         86.44                54.83         0.638          pass              0.327             56.5                           0.326                5.09             -0.050                  ok           False                  False
  CSCO           93.10               29            0.47              0.40        120.25                51.99         0.629          pass              0.718             59.6                           0.472                1.39              0.269                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-06-01T03:00:05.806892-04:00   data_refresh  data_refresh                               {'saved': 92}
2026-05-30T02:55:03.369308-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:50:06.334333-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:45:02.331534-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:40:01.232868-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:35:01.344797-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:30:06.367900-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:25:04.377495-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:20:05.639064-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:15:01.287104-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601093002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601093002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601093002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601093002)

</details>
