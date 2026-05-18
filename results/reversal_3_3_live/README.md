# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 11:00:09 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$30,295.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$-350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   1      5     14525.0                 14175.0        29.05          28.35       350.6        343.66          bid_ask_mid                      28.35                bid_ask_mid                    True          -350.0                  -2.41          97.3               37              0.63         45.67           53.57                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               34            0.69              0.53        108.54               115.99         0.706            pass              0.872             80.4                           0.504               12.77              0.774                                 ok            True                  False
  CSCO           91.30               23            1.10              0.91        117.82                49.84         0.606            pass              0.570             40.6                           0.482               26.22              2.719                                 ok            True                  False
  SNPS           95.24               21            2.05              7.22        499.32                42.05         0.525            pass              0.546              6.7                           0.121               -1.09             -0.011                                 ok            True                  False
  ASML           81.48               27            1.58             16.58       1494.70                50.55         0.501            pass              0.286             27.8                           0.360                6.63              0.541                                 ok            True                  False
   TXN           93.94               33            0.09              0.20        302.64                68.84         0.696            pass              0.873             92.7                           0.615                8.22              0.954                                 ok           False                  False
  QCOM           80.00                5            3.07              4.34        199.63                99.06         0.666            pass              0.132             21.7                           0.250               15.98              1.114                                 ok           False                  False
  INSM           66.67               27            1.92              1.47        108.51               111.34         0.648            pass              0.342             54.7                           0.564              -23.55             -2.241 downtrend_blocked_slope_and_streak           False                  False
  META           72.41               29            0.90              3.86        612.58                37.75         0.507            pass              0.370             64.2                           0.586               -0.28              0.057                                 ok           False                  False
  MCHP           88.64               44            0.18              0.12         93.80                53.01         0.504            pass              0.742             87.0                           0.552               -1.70             -0.516 downtrend_blocked_slope_and_streak           False                  False
  AVGO           92.86               28            1.24              3.70        423.61                43.18         0.496 below_threshold              0.657             48.2                           0.648                0.82              0.105                                 ok           False                  False
  KLAC           80.00               20            2.22             28.03       1792.31                50.53         0.492 below_threshold              0.219             34.5                           0.493                2.97              0.451                                 ok           False                  False
  AMGN           83.33               24            0.67              1.53        325.65                26.25         0.487 below_threshold              0.402             57.1                           0.622                0.84              0.124                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                      detail
2026-05-18T11:00:09.683441-04:00 early_entry_1100 entry_skipped                  {"reason": "no_candidate"}
2026-05-18T10:27:37.648386-04:00 early_entry_1025 entry_skipped                  {"reason": "no_candidate"}
2026-05-18T03:00:02.728743-04:00     data_refresh  data_refresh                               {'saved': 92}
2026-05-16T02:55:09.369538-04:00   share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:50:03.948678-04:00   share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:45:01.564452-04:00   share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:40:01.759045-04:00   share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:35:01.904686-04:00   share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:30:04.868117-04:00   share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:25:04.937005-04:00   share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518110009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518110009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518110009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518110009)

</details>
