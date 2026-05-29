# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:00:05 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$32,264.25`
- Equity: `$32,264.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.86               28            0.61              0.50        118.42                52.06         0.635          pass              0.694             55.9                           0.392                2.07              0.217                                 ok            True                  False
  AMGN           88.00               25            0.71              1.68        335.76                27.03         0.529          pass              0.413             15.7                           0.164                0.11              0.262                                 ok            True                  False
  INSM           77.78               45            0.13              0.10        108.33               111.11         0.779          pass              0.541             87.7                           0.670               -6.39             -0.335                                 ok           False                  False
  MELI           95.12               41            0.18              2.08       1694.64                61.27         0.617          pass              0.904             80.9                           0.604                5.30              0.819                                 ok           False                  False
   AEP           69.23               13            0.59              0.53        127.53                25.60         0.602          pass              0.101              6.8                           0.220               -1.24              0.105                                 ok           False                  False
  CTSH           91.89               37            0.15              0.06         53.83                48.05         0.555          pass              0.818             88.6                           0.576               17.59              1.397                                 ok           False                  False
  REGN           89.19               37            0.28              1.22        621.00                44.05         0.547          pass              0.699             73.1                           0.421              -12.93             -1.052 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.00               10            1.71              1.75        145.54                23.56         0.537          pass              0.322              0.4                           0.186               -3.28             -0.295            downtrend_blocked_slope           False                  False
   TXN          100.00               32            0.29              0.64        315.68                35.59         0.525          pass              0.758             53.1                           0.309                2.23              0.548                                 ok           False                  False
  SBUX           90.91               11            1.21              0.85        100.38                16.60         0.519          pass              0.533             61.3                           0.334               -5.91             -0.723            downtrend_blocked_slope           False                  False
   CSX           71.43                7            1.83              0.59         45.56                23.65         0.513          pass              0.051              0.0                           0.250               -2.07             -0.016           downtrend_blocked_streak           False                  False
  MDLZ           85.71                7            1.84              0.80         62.05                12.98         0.510          pass              0.267             21.0                           0.139                0.45              0.160                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                  detail
2026-05-29T10:00:05.402847-04:00 early_entry_1000  entry_skipped                                                                                                                                                              {"reason": "no_candidate"}
2026-05-29T09:20:06.125686-04:00     data_refresh   data_refresh                                                                                                                                                                           {'saved': 92}
2026-05-28T15:10:10.028312-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T15:05:04.986129-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T15:00:06.948836-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T14:55:06.010831-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T14:50:05.035990-04:00       entry_1500  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T14:50:05.035990-04:00       entry_1500 timing_overlay                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-28", "training_samples": 5117, "window": 5}
2026-05-28T12:40:01.998163-04:00      manage_1230           exit {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 35.95, "pnl": 1880.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.04, "ticker": "AVGO"}
2026-05-28T12:00:05.896854-04:00 early_entry_1200  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529100005)

</details>
