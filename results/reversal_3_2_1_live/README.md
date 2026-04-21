# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 09:45:06 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,851.31`
- Equity: `$12,115.32`
- Realized PnL: `$2,139.59`
- Unrealized PnL: `$-24.27`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
   HON      share share_fallback        HON       2026-04-20                   1     23     5288.28                 5264.01       229.93         228.87      229.93        228.87          -24.27                  -0.46         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               19            1.67              8.75        745.66                22.94            True
   WDC           97.37               38            0.55              1.45        373.49                71.77            True
  NVDA           91.89               37            0.55              0.77        201.73                32.81            True
  AVGO           91.67               36            0.91              2.53        398.54                44.63            True
  QCOM           90.62               32            0.83              0.80        137.18                21.00            True
  ORLY           90.48               42            0.55              0.36         92.68                22.94            True
  ASML           89.47               38            0.51              5.31       1474.22                54.76            True
   APP           85.29               34            1.56              5.36        488.66                75.05            True
  DXCM           85.29               34            1.41              0.64         64.35                35.89            True
  ISRG           85.29               34            0.92              2.99        464.32                25.78            True
   PEP           84.62               26            0.63              0.69        156.69                19.06            True
  AAPL           83.87               31            0.73              1.40        272.45                22.37            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                         detail
2026-04-21T09:40:06.428759-04:00  manage_0930 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-21T09:35:02.420022-04:00  manage_0930 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-21T09:30:06.425372-04:00  manage_0930 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-21T09:25:06.429302-04:00  manage_0930 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-21T00:00:06.440855-04:00 data_refresh data_refresh                                                                                                                                                  {'saved': 99}
2026-04-20T16:10:06.425591-04:00  manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T16:05:05.426426-04:00  manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T16:00:06.436506-04:00  manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:55:06.432735-04:00  manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:50:06.460350-04:00  manage_1600         exit {"asset_type": "share", "contract_symbol": "REGN", "fill_price": 748.9, "pnl": 19.17, "reason": "time_exit_at_4pm_scan", "return_pct": 0.29, "ticker": "REGN"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421094506)

</details>
