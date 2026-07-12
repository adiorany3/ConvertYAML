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
1. `AKUN-001-UNKNOWN-VLESS-WS-81MS` (url=334ms, nekobox=381ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-92MS` (url=340ms, nekobox=520ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-84MS` (url=341ms, nekobox=382ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-101MS` (url=378ms, nekobox=412ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=339ms, nekobox=360ms, status=yes)
6. `AKUN-006-PUBLICDOMAINREGISTRY-NET-VLESS-WS-102MS` (url=465ms, nekobox=389ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-103MS` (url=390ms, nekobox=441ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=348ms, nekobox=411ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS` (url=279ms, nekobox=426ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-129MS` (url=353ms, nekobox=432ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-123MS` (url=372ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=392ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-136MS` (url=266ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-143MS` (url=395ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-123MS` (url=342ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-126MS` (url=291ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-112MS` (url=335ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-167MS` (url=350ms, status=HTTP 204)
19. `AKUN-019-MYBB-VLESS-WS-125MS` (url=348ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-139MS` (url=381ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-116MS` (url=505ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-149MS` (url=403ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-144MS` (url=318ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-112MS` (url=381ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-311MS` (url=670ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
