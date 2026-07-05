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
1. `AKUN-001-SIN-VLESS-WS-58MS` (url=213ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=221ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=240ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=208ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=216ms, nekobox=235ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-67MS` (url=225ms, nekobox=240ms, status=yes)
7. `AKUN-007-TANG-NET-VLESS-WS-84MS` (url=207ms, nekobox=230ms, status=yes)
8. `AKUN-008-OVH-VLESS-WS-96MS` (url=239ms, nekobox=239ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS` (url=210ms, nekobox=244ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-105MS` (url=222ms, nekobox=244ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-86MS` (url=217ms, status=HTTP 204)
12. `AKUN-012-WEYRO-NET-VLESS-WS-110MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-83MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-112MS` (url=230ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-346MS` (url=740ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-384MS` (url=929ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-375MS` (url=830ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-395MS` (url=843ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-354MS` (url=727ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-371MS` (url=867ms, status=HTTP 204)
22. `AKUN-023-SPEEDTEST-VLESS-WS-350MS` (url=771ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-671MS` (url=1084ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-676MS` (url=1054ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-701MS` (url=1074ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
