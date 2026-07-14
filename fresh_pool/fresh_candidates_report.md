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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=209ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=220ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=234ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=214ms, nekobox=242ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS` (url=213ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=232ms, nekobox=233ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-88MS` (url=230ms, nekobox=250ms, status=yes)
8. `AKUN-008-VOV-VLESS-WS-101MS` (url=309ms, nekobox=277ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-110MS` (url=315ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-72MS` (url=206ms, nekobox=260ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-91MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-CZ-LOTUNA-19970206-VLESS-WS-76MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-CZ-LOTUNA-19970206-VLESS-WS-103MS` (url=233ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-97MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-PAGES-VLESS-WS-86MS` (url=199ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-108MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-132MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-89MS` (url=225ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-101MS` (url=230ms, status=HTTP 204)
21. `AKUN-022-PUBLICDOMAINREGISTRY-NET-VLESS-WS-76MS` (url=221ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-365MS` (url=777ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-353MS` (url=800ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-373MS` (url=1790ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-358MS` (url=854ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
