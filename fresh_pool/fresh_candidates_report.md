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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-91MS` (url=209ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-94MS` (url=212ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=228ms, nekobox=232ms, status=yes)
4. `AKUN-004-DIXONS-VLESS-WS-94MS` (url=240ms, nekobox=252ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-101MS` (url=214ms, nekobox=235ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-100MS` (url=212ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=209ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=217ms, nekobox=287ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=216ms, nekobox=242ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS` (url=204ms, nekobox=232ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-95MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-98MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-84MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-117MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-113MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-103MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-85MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-US-VLESS-WS-121MS` (url=254ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-111MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-164MS` (url=254ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-169MS` (url=324ms, status=HTTP 204)
23. `AKUN-023-NEXUSMODS-VLESS-WS-128MS` (url=310ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-131MS` (url=326ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-165MS` (url=316ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
