# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=229ms, nekobox=253ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-62MS` (url=219ms, nekobox=271ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=232ms, nekobox=257ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=217ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=232ms, nekobox=238ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=203ms, nekobox=179ms, status=no)
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=207ms, nekobox=190ms, status=no)
9. `AKUN-007-GO-DADDY-COM-LLC-VLESS-WS-110MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-78MS`
12. `AKUN-010-VULTR-VLESS-WS-132MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-74MS` (url=210ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-66MS` (url=252ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-363MS` (url=735ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-385MS` (url=838ms, status=HTTP 204)
17. `AKUN-018-SPEEDTEST-VLESS-WS-392MS` (url=869ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-393MS` (url=892ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-364MS` (url=790ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-412MS` (url=843ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-347MS` (url=805ms, status=HTTP 204)
22. `AKUN-031-UNKNOWN-VLESS-WS-646MS` (url=977ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-789MS` (url=1280ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-799MS` (url=1284ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
