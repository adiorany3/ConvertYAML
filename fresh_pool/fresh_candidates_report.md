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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=219ms, nekobox=247ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=213ms, nekobox=229ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=207ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=210ms, nekobox=286ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=224ms, nekobox=188ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS`
9. `AKUN-009-DEV-VLESS-WS-87MS` (url=201ms, nekobox=190ms, status=no)
10. `AKUN-010-UNKNOWN-VLESS-WS-79MS` (url=227ms, nekobox=185ms, status=no)
11. `AKUN-008-UNKNOWN-VLESS-WS-96MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-92MS` (url=209ms, nekobox=187ms, status=no)
13. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-110MS`
15. `AKUN-015-DEV-VLESS-WS-94MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-116MS` (url=200ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-105MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-118MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-87MS` (url=205ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-230MS` (url=490ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-244MS` (url=507ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-251MS` (url=548ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-242MS` (url=545ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-265MS` (url=587ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-236MS` (url=506ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
