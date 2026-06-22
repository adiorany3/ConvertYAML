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
1. `AKUN-001-UNKNOWN-VLESS-WS-75MS` (url=332ms, nekobox=314ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS`
3. `AKUN-003-VULTR-VLESS-WS-79MS`
4. `AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-79MS`
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS`
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-101MS`
7. `AKUN-008-DEV-VLESS-WS-83MS` (url=299ms, nekobox=192ms, status=no)
8. `AKUN-007-UNKNOWN-VLESS-WS-84MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-117MS` (url=279ms, nekobox=7172ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS`
11. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-112MS` (url=324ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-129MS` (url=1062ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-103MS` (url=307ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-155MS` (url=298ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-260MS` (url=680ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-299MS` (url=668ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-269MS` (url=570ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-305MS` (url=687ms, status=HTTP 204)
21. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-299MS` (url=703ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-326MS` (url=649ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-254MS` (url=559ms, status=HTTP 204)
24. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-554MS` (url=960ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-619MS` (url=904ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
