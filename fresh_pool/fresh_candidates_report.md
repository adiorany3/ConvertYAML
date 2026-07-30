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
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-IP-VLESS-WS-87MS` (url=213ms, nekobox=258ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-86MS` (url=230ms, nekobox=256ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-92MS` (url=197ms, nekobox=244ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-93MS` (url=207ms, nekobox=259ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=216ms, nekobox=301ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS`
8. `AKUN-008-UNKNOWN-VLESS-WS-89MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-125MS` (url=246ms, status=HTTP 204)
12. `AKUN-013-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-121MS` (url=1256ms, status=HTTP 204)
13. `AKUN-014-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-113MS` (url=229ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-156MS` (url=272ms, status=HTTP 204)
15. `AKUN-017-RMGYVPN-VLESS-WS-311MS` (url=647ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-356MS` (url=760ms, status=HTTP 204)
17. `AKUN-021-130209-VLESS-WS-424MS` (url=771ms, status=HTTP 204)
18. `AKUN-022-UNKNOWN-VLESS-WS-415MS` (url=978ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-449MS` (url=938ms, status=HTTP 204)
20. `AKUN-026-CLOUDFLARE-VLESS-WS-648MS` (url=983ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-712MS` (url=1451ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-739MS` (url=1201ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-705MS` (url=1114ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-282MS` (url=1257ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
