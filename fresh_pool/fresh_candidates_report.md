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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-108MS` (url=257ms, nekobox=285ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-122MS` (url=286ms, nekobox=315ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-144MS` (url=273ms, nekobox=289ms, status=yes)
4. `AKUN-004-MEDIUM-VLESS-WS-129MS` (url=270ms, nekobox=298ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-112MS` (url=258ms, nekobox=392ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-141MS` (url=249ms, nekobox=307ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-100MS` (url=308ms, nekobox=305ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-126MS` (url=514ms, nekobox=318ms, status=yes)
9. `AKUN-009-DEV-VLESS-WS-153MS` (url=239ms, nekobox=227ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-144MS`
11. `AKUN-010-EU-VLESS-WS-122MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-120MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-137MS` (url=274ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-335MS` (url=596ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-343MS` (url=741ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-339MS` (url=4238ms, status=HTTP 204)
17. `AKUN-017-CLOUDWEBMANAGE-EU-FR-VLESS-WS-141MS` (url=290ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-134MS` (url=273ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-385MS` (url=781ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-135MS` (url=264ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-485MS` (url=706ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-441MS` (url=921ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-416MS` (url=1006ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-518MS` (url=843ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-327MS` (url=770ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
