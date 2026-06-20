# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-135MS` (url=272ms, nekobox=296ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-136MS` (url=263ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-137MS` (url=262ms, nekobox=300ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-139MS` (url=284ms, nekobox=299ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-134MS` (url=268ms, nekobox=354ms, status=yes)
6. `AKUN-006-OPENAI-VLESS-WS-137MS` (url=283ms, nekobox=297ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-135MS` (url=240ms, nekobox=232ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-156MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-148MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-139MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-145MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-178MS` (url=262ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-174MS` (url=239ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-344MS` (url=699ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-343MS` (url=681ms, status=HTTP 204)
16. `AKUN-016-CONFLU-VLESS-WS-347MS` (url=672ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-379MS` (url=780ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-372MS` (url=781ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-390MS` (url=759ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-382MS` (url=759ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-517MS` (url=888ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-565MS` (url=766ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-561MS` (url=778ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-568MS` (url=767ms, status=HTTP 204)
25. `AKUN-031-BROADNNET-KR-VLESS-WS-700MS` (url=777ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
