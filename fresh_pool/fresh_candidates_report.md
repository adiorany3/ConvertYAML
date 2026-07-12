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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=234ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=236ms, nekobox=274ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=220ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=348ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-62MS` (url=235ms, nekobox=252ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-66MS` (url=248ms, nekobox=243ms, status=yes)
7. `AKUN-007-PUBLICDOMAINREGISTRY-NET-VLESS-WS-76MS` (url=219ms, nekobox=265ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-68MS` (url=220ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-67MS` (url=243ms, nekobox=255ms, status=yes)
10. `AKUN-010-HGC-GLOBAL-COMMUNICATION-VLESS-WS-97MS` (url=212ms, nekobox=257ms, status=yes)
11. `AKUN-011-HETZNER-VLESS-WS-104MS` (url=240ms, status=HTTP 204)
12. `AKUN-012-ORG-VLESS-WS-93MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-84MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-117MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-127MS` (url=281ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-155MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-63MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-106MS` (url=198ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-82MS` (url=246ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-345MS` (url=760ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-353MS` (url=743ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-348MS` (url=875ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-383MS` (url=815ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-359MS` (url=815ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-373MS` (url=824ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
