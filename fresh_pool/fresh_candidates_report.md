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
1. `AKUN-001-VULTR-VLESS-WS-84MS` (url=320ms, nekobox=343ms, status=yes)
2. `AKUN-002-NET-14-102-228-0-23-VLESS-WS-81MS` (url=286ms, nekobox=328ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=297ms, nekobox=7181ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-78MS`
6. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-97MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-127MS` (url=313ms, nekobox=7177ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-129MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-136MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS`
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-126MS` (url=309ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-105MS` (url=319ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-272MS` (url=574ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-282MS` (url=586ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-281MS` (url=562ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-298MS` (url=680ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-304MS` (url=648ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-220MS` (url=425ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-326MS` (url=625ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-401MS` (url=511ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-263MS` (url=587ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-616MS` (url=4068ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-658MS` (url=1087ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
