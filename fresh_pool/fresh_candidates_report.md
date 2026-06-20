# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=229ms, nekobox=264ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-71MS` (url=210ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=220ms, nekobox=259ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-72MS` (url=214ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=224ms, nekobox=228ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=195ms, nekobox=244ms, status=yes)
7. `AKUN-007-VULTR-VLESS-WS-67MS` (url=225ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=214ms, nekobox=245ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-74MS` (url=228ms, nekobox=250ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=221ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=280ms, status=HTTP 204)
12. `AKUN-014-CONFLU-VLESS-WS-346MS` (url=749ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-372MS` (url=783ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-375MS` (url=1147ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-401MS` (url=844ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-397MS` (url=889ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-398MS` (url=839ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-400MS` (url=877ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-619MS` (url=751ms, status=HTTP 204)
20. `AKUN-027-UNKNOWN-VLESS-WS-664MS` (url=1049ms, status=HTTP 204)
21. `AKUN-030-CLOUDFLARE-VLESS-WS-635MS` (url=944ms, status=HTTP 204)
22. `AKUN-032-UNKNOWN-VLESS-WS-679MS` (url=818ms, status=HTTP 204)
23. `AKUN-034-CLOUDFLARE-VLESS-WS-657MS` (url=896ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
