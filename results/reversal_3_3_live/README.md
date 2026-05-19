# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 14:45:04 EDT`
Last processed slot: `manual`

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

- Cash: `$26,462.75`
- Equity: `$26,462.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-19)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  TTWO     option         option TTWO260618C00250000     10          2026-05-18         2026-05-19       13.550     12.1950 -1355.00       -10.0 stop_loss_hit_at_scan
  PANW     option         option PANW260618C00250000      9          2026-05-19         2026-05-19       15.275     13.7475 -1374.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  QCOM           93.33               15            2.31              3.29        202.23                99.05         0.681          pass              0.645             62.8                           0.571                6.64              0.218                                 ok            True                  False
  GOOG           81.82               11            1.79              4.92        391.00                40.55         0.572          pass              0.204             30.5                           0.241                0.47              0.018                                 ok            True                  False
 GOOGL           81.82               11            1.86              5.17        394.73                40.53         0.570          pass              0.208             31.8                           0.253                0.29              0.028                                 ok            True                  False
   KDP           88.00               25            0.95              0.20         29.35                33.71         0.549          pass              0.421             17.6                           0.289                0.80              0.220                                 ok            True                  False
  ASML           84.38               32            0.68              7.03       1469.38                50.95         0.544          pass              0.521             67.7                           0.448                1.35             -0.140                                 ok            True                  False
  SNPS           97.14               35            0.70              2.45        497.38                41.65         0.534          pass              0.786             55.4                           0.501               -1.51             -0.163                                 ok            True                  False
  TTWO          100.00               15            1.85              3.14        240.81                33.10         0.519          pass              0.570             28.3                           0.367                6.53              1.020                                 ok            True                  False
  AVGO           89.47               19            2.20              6.47        417.94                42.85         0.507          pass              0.477             37.7                           0.350               -3.72             -0.115                                 ok            True                  False
 CMCSA           84.00               25            0.67              0.12         24.88                60.09         0.663          pass              0.354             27.2                           0.292               -6.42             -0.693 downtrend_blocked_slope_and_streak           False                  False
  CSCO           88.89                9            1.84              1.53        118.22                49.96         0.635          pass              0.440             46.5                           0.385               23.74              2.948                                 ok           False                  False
  SHOP           83.72               43            0.27              0.20        102.31                78.89         0.607          pass              0.610             83.2                           0.574               -5.13             -0.934 downtrend_blocked_slope_and_streak           False                  False
  TEAM           89.66               29            2.85              1.78         88.67               113.67         0.605          pass              0.536             30.4                           0.472               -5.91             -0.699 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                               detail
2026-05-19T12:20:01.028030-04:00      manage_1230          exit {"asset_type": "option", "contract_symbol": "PANW260618C00250000", "fill_price": 13.7475, "pnl": -1374.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PANW"}
2026-05-19T12:00:03.873446-04:00 early_entry_1200 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:55:04.964087-04:00 early_entry_1155 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:50:03.963905-04:00 early_entry_1150 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:45:02.013628-04:00 early_entry_1145 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:40:06.318992-04:00 early_entry_1140 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:35:01.898801-04:00 early_entry_1135 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:30:01.060546-04:00 early_entry_1130 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:25:05.065733-04:00 early_entry_1125 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:20:06.455937-04:00 early_entry_1120 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519144504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519144504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519144504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519144504)

</details>
